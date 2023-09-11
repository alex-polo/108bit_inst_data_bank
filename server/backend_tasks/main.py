import dataclasses
import json
import logging.config
import os
import traceback

from celery import Celery
from celery.schedules import crontab

from main.backend_tasks import synchronization_db
from main.backend_tasks.resources_list import resources
from main.database import registry_database
from main.etc import get_celery_config, CeleryConfig, get_database_config, DatabaseConfig


# Получаем базы данных брокера и бекэнда для celery из ..env
celery_config: CeleryConfig = get_celery_config()
database_config: DatabaseConfig = get_database_config()


# Конфигурация логгера
logging.config.fileConfig(celery_config.logging_config)
logger = logging.getLogger(__name__)


# Инициализируем celery
app = Celery(__name__, broker=celery_config.broker, backend=celery_config.backend)
app.config_from_object('etc.celeryconfig')


# Автопоиск задач
app.autodiscover_tasks()


def creating_periodic_tasks() -> None:
    for resource in resources:
        app.conf.beat_schedule = {
                    'task_bolid_data_collection': {
                        'task': 'backend_tasks.v1.bolid.bolid_data_collection',
                        'schedule': crontab(minute=f'*/{resource.time_execute}'),
                        'options': {
                            'routing_key': 'task_data_collection',
                            'priority': 10
                        },
                        # 'args': (16, 16),
                    },
                }


# При запуске celery выполняем
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    registry_database(database_config=database_config)

    celery_type = os.environ.get('CELERY_TYPE')
    if celery_type == 'BEAT':
        # Синхронизация списка интернет ресурсов с базой данных
        try:
            # Создаем задачу для синхронизации списка интернет ресурсов с базой данных
            logger.info('Start synchronization_db resources list with database')
            json_resources_list = json.dumps([dataclasses.asdict(obj) for obj in resources], ensure_ascii=False)

            synchronization = synchronization_db.task_synchronization_database.apply_async(args=(json_resources_list,),
                                                                                           queue='default')

            # synchronization = synchronization_db.task_synchronization_database.apply_async(args=(resources,),
            #                                                                                queue='default')

            # Ждем выполнения задачи для синхронизации
            logger.info('Waiting for a task "synchronization_db" to complete')
            if synchronization.get():
                logger.info('Creating scheduled Tasks')
                creating_periodic_tasks()
                logger.info('Scheduled tasks created')
            else:
                logger.error('Failed to create scheduled tasks')

            logger.info(f'Celery {celery_type.title()} configuration completed')
        except Exception as error:
            logger.error(error)
            logger.error(traceback.format_exc(limit=None, chain=True))
            logger.warning('Configuration completed with errors')
