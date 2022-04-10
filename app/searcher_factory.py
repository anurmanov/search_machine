import os
from app.searchers.base_searcher import Searcher
from app.searchers.json.json_searcher import JsonSearcher


def searcher_factory(type: str) -> Searcher:
    if type == 'json':
        return JsonSearcher(os.environ['JSON_DIR'])
    #elif type == 'postresql':
    #    return PostgresqlSearcher()


searcher = searcher_factory(os.environ['SEARCHER'])

