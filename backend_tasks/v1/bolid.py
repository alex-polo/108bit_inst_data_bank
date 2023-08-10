import asyncio
import logging
import traceback

import requests
from celery import shared_task
from bs4 import BeautifulSoup

from backend_tasks.misc import download
from backend_tasks.misc.classes import DownloadedContent

logger = logging.getLogger('backend')


async def main(url: str, timeout: int = 60, headers: dict = None) -> None:
    logger.info(f'Bolid tasks. Download main page')
    response: DownloadedContent = await download(url=url, timeout=timeout, headers=headers)
    if response.is_success:
        main_menu = BeautifulSoup(response.content, 'html.parser').find_all('ul',
                                                                            class_='gead_menu')

        # print(main_menu)


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
        timeout = 60
        headers = None

        logger.info(f'Starting "{name_task}" task, time: ')
        asyncio.run(main(
            url=url,
            timeout=timeout,
            headers=headers
        ))
        logger.info(f'End {name_task} task, time: ')
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))
