from abc import ABC
from typing import Optional, List


class Searcher(ABC):
    def _connect(self, *args, **kwargs) -> dict:
        """
        This private method must contain a logic
        of the connecting to the storage for searching in
        """
        raise NotImplementedError('_connect method is not implemented!')

    def search(self, payload: dict) -> dict:
        raise NotImplementedError('search method is not implemented!')

