import logging
import traceback

import src

logger = logging.getLogger()


if __name__ == '__main__':
    try:
        src.run()
    except (KeyboardInterrupt, SystemExit):
        logger.error("Server stopped!")
    except Exception as ex:
        logger.error(ex)
        logger.error(traceback.format_exc(limit=None, chain=True))
