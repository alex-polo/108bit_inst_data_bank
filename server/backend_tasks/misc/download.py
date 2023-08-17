import logging

import aiohttp

from server.backend_tasks.misc.classes import DownloadedContent

logger = logging.getLogger('backend')


async def parsing_contact_page():
    pass


async def parsing_products():
    pass


async def parsing_projects_and_solutions():
    pass


async def download(url: str, timeout: int = 60, headers: dict = None) -> DownloadedContent:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, timeout=timeout, headers=headers) as response:
            if response.status == 200:
                return DownloadedContent(is_success=True, content=await response.text())
            else:
                logger.error(f'Failed to download site content, url: "{url}", response code: "{response.status}"')
                return DownloadedContent(is_success=False, content=None)
