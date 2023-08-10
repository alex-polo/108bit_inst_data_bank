import json
import logging
import traceback
from select import select
from typing import List

from celery import shared_task
from sqlalchemy.ext.asyncio import AsyncSession

import database.main
from backend_tasks.misc.classes import ResourcesVendor

logger = logging.getLogger('backend')


async def _synchronization(resources: List[ResourcesVendor], session: AsyncSession = database.main.get_async_session()):
    select()


@shared_task()
def task_synchronization_database(resources) -> bool:
    try:
        logger.info('Start task synchronization vendors with database')
        resources_list: List[ResourcesVendor] = [ResourcesVendor(**data_dict) for data_dict in json.loads(resources)]

        return True
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))
        return False
