import asyncio
import logging
import traceback

from celery import shared_task
from bs4 import BeautifulSoup

import database
from backend_tasks.misc import download
from backend_tasks.misc.classes import DownloadedContent

logger = logging.getLogger('backend')


async def main(url: str, timeout: int = 60, headers: dict = None) -> None:
    logger.info(f'Bolid tasks. Download main page')
    response: DownloadedContent = await download(url=url, timeout=timeout, headers=headers)
    if response.is_success:
        main_menu = BeautifulSoup(response.content, 'html.parser').find_all('ul',
                                                                            class_='gead_menu')

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
                    logger.warning('Close DB session')

        # print(main_menu)


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
