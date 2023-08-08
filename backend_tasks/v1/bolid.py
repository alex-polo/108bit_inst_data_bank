import asyncio
import logging
import traceback

import requests
from celery import shared_task
from bs4 import BeautifulSoup

logger = logging.getLogger('backend')


async def main() -> None:
    for _ in range(100):
        await asyncio.sleep(1)
        logger.info('Main bolid task')
    # content_page = BeautifulSoup(page_body, 'html.parser').find_all('div', class_=items_class_name)
    # print(type(requests.get(url=url).text))
    # print(type(requests.get(url=url).content))
    # print('*' * 100)
    # import requests
    # answer = requests.get('https://bolid.ru/support/download/?groupsID=4')
    # logger.info(answer)


@shared_task()
def bolid_data_collection() -> None:
    try:
        name_task = 'bolid'
        url = 'https://bolid.ru/'
        logger.info(f'Starting "{name_task}" task, time: ')
        asyncio.run(main())
        logger.info(f'End {name_task} task, time: ')
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))


