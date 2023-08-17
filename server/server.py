import logging

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server import database
from server.database import registry_database
from server.etc import DatabaseConfig, get_database_config

logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
async def startup(session: AsyncSession = Depends(database.get_async_session)) -> None:
    pass


def registry_routers() -> None:
    pass


def run(host: str = '0.0.0.0', port: int = 8000) -> None:
    db_config: DatabaseConfig = get_database_config()
    version = registry_database(database_config=db_config)
    logger.info(f'Registry database engine, sqlalchemy version: {version}')
    uvicorn.run(app, host=host, port=port, log_config=None)
