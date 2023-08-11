from typing import Optional, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from etc.classes import DatabaseConfig


class Base(DeclarativeBase):
    pass


metadata = Base.metadata
_engine: AsyncEngine = Optional[None]
_async_session_maker: async_sessionmaker = Optional[None]


def get_session_maker():
    return _async_session_maker


async def get_api_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with _async_session_maker() as session:
        yield session


async def get_async_session() -> AsyncSession:
    async with _async_session_maker() as session:
        return session


def registry_database(database_config: DatabaseConfig) -> None:
    global _engine, _async_session_maker

    database_url = f'postgresql+asyncpg://' \
                   f'{database_config.db_user}:' \
                   f'{database_config.db_pass}@' \
                   f'{database_config.db_host}:' \
                   f'{database_config.db_port}/' \
                   f'{database_config.db_name}'

    _engine = create_async_engine(database_url)
    _async_session_maker = async_sessionmaker(_engine, class_=AsyncSession, expire_on_commit=False)
