from typing import Optional
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .schemes import Payload
from .searcher_factory import searcher
from .statistics import Statistics
from app.searchers.json.constants import USERS, TICKETS, ORGANIZATIONS


app = FastAPI()


@app.post('/search', status_code=200)
async def search_endpoint(payload: Payload) -> JSONResponse:
    search_result = searcher.search(payload.dict())
    Statistics.count_of_requests += 1
    return JSONResponse(content=search_result, status_code=200)


@app.get('/show_fields/{entity}', status_code=200)
async def show_fields_endpoint(entity: Optional[str] = None) -> JSONResponse:
    if entity in (USERS, TICKETS, ORGANIZATIONS):
        try:
            first_record = searcher.get_record_by_index(entity, 0)
            list_of_fields = list(first_record.keys())
            print(list_of_fields)
            return JSONResponse(content=list_of_fields, status_code=200)
        except KeyError:
            raise HTTPException(status_code=404,
                                detail=f"Entity '{entity}' doesn't exists!")
        except IndexError:
            raise HTTPException(status_code=404,
                                detail=f"There are no records in the entity '{entity}'!")

    else:
        raise HTTPException(status_code=404, detail=f"Entity '{entity}' doesn't exists!")


@app.get('/show_entities', status_code=200)
async def show_entities_endpoint() -> JSONResponse:
    return JSONResponse(content=[USERS, TICKETS, ORGANIZATIONS], status_code=200)


@app.get('/stats', status_code=200)
async def stats_endpoint() -> JSONResponse:
    """
    Endpoint for providing statistics about the worker
    """
    duration = datetime.now() - Statistics.start_time

    d = {}
    d['days'], remaining = divmod(duration.total_seconds(), 86400)
    d['hours'], remaining = divmod(remaining, 3600)
    d['minutes'], d['seconds'] = divmod(remaining, 60)

    stats = {
        'count_of_requests': Statistics.count_of_requests,
        'uptime': f"{d['days']:n} d, {d['hours']:n} hr, {d['minutes']:n} min, {int(d['seconds'])} sec"
    }
    return JSONResponse(content=stats, status_code=200)


@app.on_event('startup')
def startup_event():
    """
    Clear statistics on startup
    """
    Statistics.count_of_requests = 0
    Statistics.start_time = datetime.now()


@app.on_event('shutdown')
def shutdown_event():
    """
    Clear statistics on shutdown
    """
    Statistics.count_of_requests = 0

