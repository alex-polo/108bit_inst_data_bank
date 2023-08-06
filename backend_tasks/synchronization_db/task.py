import logging
from typing import List

from celery import shared_task

from backend_tasks.resources.tools.classes import ResourcesVendor

logger = logging.getLogger(__name__)


@shared_task
def task_synchronization_database(resources: List[ResourcesVendor]):
    logger.debug(resources)
    return True


def synchronization(resources_list: List[ResourcesVendor]) -> bool:
    logger.info('synchronization')
    result = task_synchronization_database.apply_async(args=(resources_list,), queue='default')
    # task_result = result.get()
    # task_status = result.status

    return True
