import logging
import traceback
from typing import List

from celery import shared_task

from backend_tasks.resources.tools.classes import ResourcesVendor

logger = logging.getLogger('backend')


@shared_task
def task_synchronization_database(resources: List[ResourcesVendor]) -> bool:
    print(1)
    try:
        logger.info('Start synchronization_db resources list with database')
        return True
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))

