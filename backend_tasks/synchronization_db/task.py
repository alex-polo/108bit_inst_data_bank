import logging
import traceback
from typing import List

from celery import shared_task

from backend_tasks.misc.classes import ResourcesVendor

logger = logging.getLogger('backend')


@shared_task
def task_synchronization_database(resources: List[ResourcesVendor]) -> bool:
    try:
        return True
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))

