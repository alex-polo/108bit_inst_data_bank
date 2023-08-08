import logging

from celery import shared_task

logger = logging.getLogger('backend')


@shared_task()
def bolid_data_collection() -> None:
    logger.info('Starting Bolid task')
    import requests
    answer = requests.get('https://bolid.ru/support/download/?groupsID=4')
    logger.info(answer)
    logger.info('End Bolid task')
