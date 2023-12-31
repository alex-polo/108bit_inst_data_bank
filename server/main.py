import logging
import time

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from database import get_async_session, registry_database
from database.models import Sites
from etc import DatabaseConfig, get_database_config

logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup(session: AsyncSession = Depends(get_async_session)) -> None:
    pass


def registry_routers() -> None:
    pass


@app.get('/')
async def home(session: AsyncSession = Depends(get_async_session)):
    try:
        # res = await session.execute(select(Sites))
        return JSONResponse(status_code=200, content={'app': 'Data Bank', 'version': '0.01a', 'data': 'any data'})
    except Exception as error:
        raise HTTPException(status_code=500, detail={
                'app': 'Data Bank',
                'version': 0.01,
                'data': error
            })


def run(host: str = '0.0.0.0', port: int = 8000) -> None:
    # db_config: DatabaseConfig = get_database_config()
    # version = registry_database(database_config=db_config)
    # logger.info(f'Registry database engine, sqlalchemy version: {version}')
    uvicorn.run(app, host=host, port=port, log_config=None)
