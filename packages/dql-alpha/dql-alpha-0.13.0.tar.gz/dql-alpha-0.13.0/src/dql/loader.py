from typing import List, Optional

from dql.catalog import Catalog
from dql.data_storage.sqlite import SQLiteDataStorage
from dql.dataset import DatasetRow


class DataView:
    def __init__(
        self,
        contents: List[DatasetRow],
        reader,
        transform,
        catalog: Optional[Catalog] = None,
        client_config=None,
    ):
        self.contents = contents
        self.reader = reader
        self.transform = transform
        if catalog is None:
            catalog = Catalog(SQLiteDataStorage())
        self.catalog = catalog
        self.client_config = client_config or {}

    @classmethod
    def from_dataset(
        cls, name: str, reader, transform, *, catalog=None, client_config=None
    ):
        if catalog is None:
            catalog = Catalog(SQLiteDataStorage())
        contents = list(catalog.ls_dataset_rows(name))
        return cls(contents, reader, transform, catalog, client_config)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, i):
        row = self.contents[i]
        sample = self.catalog.read_object(row, self.reader, **self.client_config)
        return self.transform(row, sample)
