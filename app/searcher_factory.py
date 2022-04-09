import os
from worker.searchers.base_searcher import Searcher
from worker.searchers.json.json_searcher import JsonSearcher


def searcher_factory(type: str) -> Searcher:
    if type == 'json':
        return JsonSearcher()
    #elif type == 'postresql':
    #    return PostgresqlSearcher()


searcher = searcher_factory(os.environ['SEARCHER'])

