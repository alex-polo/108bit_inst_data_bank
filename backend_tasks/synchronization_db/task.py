import asyncio
import json
import logging
import traceback
from typing import List

from celery import shared_task
from sqlalchemy import select, ChunkedIteratorResult

import database.main
from backend_tasks.misc.classes import ResourcesVendor
from database.models import Sites

logger = logging.getLogger('backend')


async def _synchronization(resources: List[ResourcesVendor]):
    async with await database.get_async_session() as session:
        async with session.begin():
            result = await session.execute(select(Sites))
            print(type(result))
            print(result)


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
