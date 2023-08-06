import os

from environs import Env

from etc import CeleryConfig
from etc.settings import celery_logging_config

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'


def get_celery_config() -> CeleryConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return CeleryConfig(
        logging_config=celery_logging_config,
        broker=env.str('CELERY_BROKER'),
        backend=env.str('CELERY_BACKEND'),
    )
