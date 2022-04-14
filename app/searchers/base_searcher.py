from abc import ABC


class Searcher(ABC):
    def _connect(self, *args, **kwargs) -> dict:
        """
        This private method must contain a logic
        of the connecting to the storage for searching in.
        Must be called from __init__()
        One searcher holds one connection.
        """
        raise NotImplementedError('_connect method is not implemented!')

    def search(self, payload: dict) -> dict:
        raise NotImplementedError('search method is not implemented!')

    def get_record_by_index(self, entity: str, index: int = 0) -> dict:
        raise NotImplementedError('get_record_by_index method is not implemented!')
