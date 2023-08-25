import logging

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

import database
from server.etc import DatabaseConfig, get_database_config

logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
async def startup(session: AsyncSession = Depends(database.get_async_session)) -> None:
    pass


def registry_routers() -> None:
    pass


@app.get('/')
def home():
    try:
        return JSONResponse(status_code=200, content={'app': 'Data Bank', 'version': 0.01, 'data': None})
    except Exception as error:
        raise HTTPException(status_code=500, detail={
                'app': 'Data Bank',
                'version': 0.01,
                'data': error
            })


def run(host: str = '0.0.0.0', port: int = 8000) -> None:
    db_config: DatabaseConfig = get_database_config()
    version = database.registry_database(database_config=db_config)
    logger.info(f'Registry database engine, sqlalchemy version: {version}')
    uvicorn.run(app, host=host, port=port, log_config=None)
