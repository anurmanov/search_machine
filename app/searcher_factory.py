import os
from app.searchers.base_searcher import Searcher
from app.searchers.json.json_searcher import JsonSearcher


def searcher_factory(type: str) -> Searcher:
    """
    This factory function creates an object-inheritant of the Searcher class
    according to the required type of the searcher ('json',
    might be 'postgres' in the potential future)
    :param type: type of the searcher
    :return: an object-inheritant of the Searcher class
    """
    if type == 'json':
        return JsonSearcher(os.environ['JSON_DIR'])
    #elif type == 'postres':
    #    return PostgresqlSearcher()


searcher = searcher_factory(os.environ['SEARCHER'])

