from ram_logger import RamLogger
from sql_connector import SqlConnection
from fastapi import FastAPI
from fastapi.responses import JSONResponse

ram_app = FastAPI()
sql_connection = SqlConnection('ram.db')
ram_logger = RamLogger('ram.db')


@ram_app.on_event("startup")
async def startup_event():
    ram_logger.start_logging()


@ram_app.on_event("shutdown")
def shutdown_event():
    ram_logger.stop_logging()


@ram_app.get("/logs/")
async def last_statuses(number: int):
    data = sql_connection.get_last_status(number)
    response = []
    for i in data:
        response.append({"total": i[0], "used": i[1], "free": i[2]})

    return JSONResponse(response)
