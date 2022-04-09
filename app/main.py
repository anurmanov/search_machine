from datetime import datetime
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from .searcher_factory import searcher
from .statistics import Statistics


app = FastAPI()


@app.post('/search', status_code=200)
async def search_endpoint(payload: dict = Body()) -> JSONResponse:
    search_result = searcher.search(payload)
    Statistics.count_of_requests += 1
    return JSONResponse(content=search_result, status_code=200)


@app.get('/stats', status_code=200)
async def stats_endpoint() -> JSONResponse:
    duration = datetime.now() - Statistics.start_time

    d = {}
    d['days'], remaining = divmod(duration.total_seconds(), 86400)
    d['hours'], remaining = divmod(remaining, 3600)
    d['minutes'], d['seconds'] = divmod(remaining, 60)

    stats = {
        'count_of_requests': Statistics.count_of_requests,
        'uptime': f"{d['days']} d, {d['hours']} hr, {d['minutes']} min, {d['seconds']} sec"
    }
    return JSONResponse(content=stats, status_code=200)


@app.on_event('startup')
def startup_event():
    Statistics.count_of_requests = 0
    Statistics.start_time = datetime.now()


@app.on_event('shutdown')
def shutdown_event():
    Statistics.count_of_requests = 0
    Statistics.start_time = datetime.now()

