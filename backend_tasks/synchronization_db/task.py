import asyncio
import json
import logging
import traceback
from typing import List, AsyncGenerator

from celery import shared_task
from sqlalchemy import select, ChunkedIteratorResult
from sqlalchemy.ext.asyncio import AsyncSession

import database.main
from backend_tasks.misc.classes import ResourcesVendor
from database.models import Sites

logger = logging.getLogger('backend')


async def _synchronization(resources: List[ResourcesVendor]):
    async for session in database.get_async_session():
        async with session.begin():
            try:
                # Работа с асинхронной сессией и объектами
                # result = session.execute()
                await session.commit()
            except Exception as error:
                await session.rollback()
                logger.error(error)
                logger.error(traceback.format_exc(limit=None, chain=True))
            finally:
                await session.close()


@shared_task()
def task_synchronization_database(resources) -> bool:
    try:
        logger.info('Start task synchronization vendors with database')
        resources_list: List[ResourcesVendor] = [ResourcesVendor(**data_dict) for data_dict in json.loads(resources)]
        asyncio.run(_synchronization(resources=resources))
        return True
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))
        return False
