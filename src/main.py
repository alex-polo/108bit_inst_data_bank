import logging

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import database
from database import registry_database
from etc import DatabaseConfig, get_database_config

logger = logging.getLogger()

app = FastAPI()


@app.on_event("startup")
async def startup(session: AsyncSession = Depends(database.get_async_session)) -> None:
    pass


def registry_routers() -> None:
    pass


def run():
    db_config: DatabaseConfig = get_database_config()
    registry_database(database_config=db_config)

    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
