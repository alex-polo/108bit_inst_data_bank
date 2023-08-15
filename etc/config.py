import os

from environs import Env

from etc import CeleryConfig, DatabaseConfig
from etc.settings import celery_logging_config, etc_directory


def get_celery_config() -> CeleryConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))
    etc_dir = os.path.join(os.getcwd(), etc_directory)

    return CeleryConfig(
        logging_config=os.path.join(etc_dir, celery_logging_config),
        broker=env.str('CELERY_BROKER'),
        backend=env.str('CELERY_BACKEND'),
    )


def get_database_config() -> DatabaseConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return DatabaseConfig(
        db_user=env.str('DB_USER'),
        db_pass=env.str('DB_PASS'),
        db_host=env.str('DB_HOST'),
        db_port=env.str('DB_PORT'),
        db_name=env.str('DB_NAME'),
    )
