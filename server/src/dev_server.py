import logging
import traceback

from main import src

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    try:
        logger.info('Running fastapi server')
        src.run()
    except (KeyboardInterrupt, SystemExit):
        logger.error("Server stopped!")
    except Exception as ex:
        logger.error(ex)
        logger.error(traceback.format_exc(limit=None, chain=True))
