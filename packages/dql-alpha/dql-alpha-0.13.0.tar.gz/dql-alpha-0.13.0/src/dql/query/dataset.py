import random
import string
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable, List

import sqlalchemy
from sqlalchemy import sql

from dql.catalog import Catalog
from dql.data_storage.sqlite import SQLiteDataStorage, compile_statement
from dql.dataset import core_dataset_columns
from dql.query.schema import create_udf_table

if TYPE_CHECKING:
    from sqlalchemy.sql.base import Executable
    from sqlalchemy.sql.elements import ColumnElement

    from dql.query.udf import UDF


class Step(ABC):
    """A query processing step (filtering, mutation, etc.)"""

    @abstractmethod
    def apply(self, query: "Executable", conn) -> "QueryGenerator":
        """Apply the processing step."""


class QueryGenerator:
    def __init__(self, func, columns):
        self.func = func
        self.columns = columns

    def exclude(self, column_names):
        return self.func(*[c for c in self.columns if c.name not in column_names])

    def select(self, column_names=None):
        if column_names is None:
            return self.func(*self.columns)
        return self.func(*[c for c in self.columns if c.name in column_names])


class UDFSignal(Step):
    """Add a custom column to the result set."""

    def __init__(self, name: str, udf: "UDF"):
        self.name = name
        self.udf = udf

    def clone(self):
        return self.__class__(self.name, self.udf)

    def apply(self, query, conn):
        temp_table_name = f"udf_{self.name}"
        col = sqlalchemy.Column(self.name, self.udf.output_type, nullable=True)
        tbl = create_udf_table(
            conn,
            temp_table_name,
            [col],
        )
        selected_columns = [c.name for c in query.selected_columns]
        results = conn.execute(*compile_statement(query))
        for row in results:
            cols = {c: v for c, v in zip(selected_columns, row)}
            signal = {self.name: self.udf(cols)}
            update = tbl.insert().values(id=cols["id"], **signal)
            conn.execute(*compile_statement(update))

        # Construct a new query that will join the udf-generated partial table.
        subq = query.subquery()

        def q(*columns):
            cols1 = []
            cols2 = []
            for c in columns:
                if c.name == col.name:
                    cols2.append(c)
                else:
                    cols1.append(c)

            if cols2:
                return (
                    sqlalchemy.select(*cols1)
                    .select_from(subq)
                    .join(tbl, tbl.c.id == subq.c.id)
                    .add_columns(*cols2)
                )
            return sqlalchemy.select(*cols1).select_from(subq)

        return QueryGenerator(q, [*subq.c, col])


class SQLFilter(Step):
    def __init__(self, *args):  # pylint: disable=super-init-not-called
        self.expressions = args

    def __and__(self, other):
        return self.__class__(*(self.expressions + other))

    def clone(self):
        return self.__class__(*self.expressions)

    def apply(self, query, conn):
        new_query = query.filter(*self.expressions)

        def q(*columns):
            return new_query.with_only_columns(*columns)

        return QueryGenerator(q, new_query.selected_columns)


class SQLUnion(Step):
    def __init__(self, query1, query2):
        self.query1 = query1
        self.query2 = query2

    def apply(self, query, conn):
        q1 = self.query1.apply_steps().select().subquery()
        q2 = self.query2.apply_steps().select().subquery()
        columns1, columns2 = fill_columns(q1.columns, q2.columns)

        def q(*columns):
            names = {c.name for c in columns}
            col1 = [c for c in columns1 if c.name in names]
            col2 = [c for c in columns2 if c.name in names]
            return (
                sqlalchemy.select(*col1)
                .select_from(q1)
                .union(sqlalchemy.select(*col2).select_from(q2))
            )

        return QueryGenerator(q, columns1)


def fill_columns(
    *column_iterables: Iterable["ColumnElement"],
) -> List[List["ColumnElement"]]:
    column_dicts = [{c.name: c for c in columns} for columns in column_iterables]
    combined_columns = {n: c for col_dict in column_dicts for n, c in col_dict.items()}

    result: List[List["ColumnElement"]] = [[] for _ in column_dicts]
    for n in combined_columns:
        col = next(col_dict[n] for col_dict in column_dicts if n in col_dict)
        for col_dict, out in zip(column_dicts, result):
            if n in col_dict:
                out.append(col_dict[n])
            else:
                # Cast the NULL to ensure all columns are aware of their type
                # Label it to ensure it's aware of its name
                out.append(sqlalchemy.cast(sqlalchemy.null(), col.type).label(n))
    return result


class SQLQuery:
    def __init__(
        self, table: str = "", engine=None
    ):  # pylint: disable=super-init-not-called
        self.engine = engine
        self.steps: List["Step"] = []
        self.table = table

    def __iter__(self):
        return iter(self.results())

    def __or__(self, other):
        return self.union(other)

    def __base_query(self, engine):
        """Return the query for the table the query refers to."""
        tbl = sqlalchemy.Table(self.table, sqlalchemy.MetaData(), autoload_with=engine)

        def q(*columns):
            return sqlalchemy.select(*columns).select_from(tbl)

        return QueryGenerator(q, tbl.c)

    def apply_steps(self):
        """
        Apply the steps in the query and return the resulting
        sqlalchemy.Executable.
        """
        engine = self.engine
        query = self.__base_query(engine)
        with engine.connect() as connection:
            # use the sqlite3 dbapi directly for consistency with
            # SQLiteDataStorage, until we can use sqlalchemy
            # connections for everything
            conn = connection.connection.driver_connection
            for step in self.steps:
                query = step.apply(
                    query.select(), conn
                )  # a chain of steps linked by results
        return query

    def results(self):
        engine = self.engine
        query = self.apply_steps()
        with engine.connect() as connection:
            conn = connection.connection.driver_connection
            result = conn.execute(*compile_statement(query.select())).fetchall()
        return result

    def clone(self):
        obj = self.__class__()
        obj.engine = self.engine
        obj.table = self.table
        obj.steps = self.steps.copy()
        return obj

    def filter(self, *args):
        query = self.clone()
        steps = query.steps
        if steps and isinstance(steps[-1], SQLFilter):
            steps[-1] = steps[-1] & args
        else:
            steps.append(SQLFilter(*args))
        return query

    def union(self, dataset_query):
        left = self.clone()
        right = dataset_query.clone()
        new_query = self.clone()
        new_query.steps = [SQLUnion(left, right)]
        return new_query


class DatasetQuery(SQLQuery):
    def __init__(self, path: str = "", name: str = "", catalog=None):
        if catalog is None:
            catalog = Catalog(SQLiteDataStorage())
        self.catalog = catalog

        data_storage = catalog.data_storage
        table = ""
        if path:
            # TODO add indexing step
            raise NotImplementedError("path not supported")
        elif name:
            if catalog is None:
                raise ValueError("using name requires catalog")
            table = data_storage._dataset_table_name(data_storage.get_dataset(name).id)
        super().__init__(table=table, engine=data_storage.engine)

    def clone(self):
        obj = self.__class__(catalog=self.catalog)
        obj.engine = self.engine
        obj.table = self.table
        obj.steps = self.steps.copy()
        return obj

    def add_signal(self, name: str, udf: "UDF"):
        query = self.clone()
        steps = query.steps
        steps.append(UDFSignal(name, udf))
        return query

    def save(self, name: str):
        """Save the query as a shadow dataset."""

        engine = self.engine
        query = self.apply_steps()

        # Save to a temporary table first.
        temp_tbl = f"tmp_{name}_" + _random_string(6)
        columns: List["sqlalchemy.Column"] = [
            sqlalchemy.Column(col.name, col.type)
            for col in query.columns
            if col.name not in CORE_COLUMN_NAMES
        ]
        self.catalog.data_storage.create_dataset_rows_table(
            temp_tbl,
            custom_columns=columns,
            if_not_exists=False,
        )
        tbl = sqlalchemy.Table(temp_tbl, sqlalchemy.MetaData(), autoload_with=engine)
        # Exclude the id column and let the db create it to avoid unique
        # constraint violations
        cols = [col.name for col in tbl.c if col.name != "id"]
        with engine.connect() as connection:
            conn = connection.connection.driver_connection
            conn.execute(
                *compile_statement(
                    sqlalchemy.insert(tbl).from_select(cols, query.exclude("id"))
                )
            )

        # Create a shadow dataset.
        self.catalog.data_storage.create_shadow_dataset(name, create_rows=False)
        dataset = self.catalog.data_storage.get_dataset(name)
        # pylint: disable=protected-access
        table_name = self.catalog.data_storage._dataset_table_name(dataset.id)
        with self.engine.connect() as connection:
            conn = connection.connection.driver_connection
            conn.execute(
                *compile_statement(
                    sql.text(f"ALTER TABLE {temp_tbl} RENAME TO {table_name}")
                )
            )


def _random_string(length: int) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits)  # nosec B311
        for i in range(length)
    )


CORE_COLUMN_NAMES = [col.name for col in core_dataset_columns()]
