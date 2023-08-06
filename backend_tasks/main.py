import logging.config
import os
import traceback

from celery import Celery

from backend_tasks import synchronization_db, misc
from backend_tasks.resources.sites import resources_list
from etc import get_celery_config, CeleryConfig

# Получаем базы данных брокера и бекэнда для celery из .env
celery_config: CeleryConfig = get_celery_config()

# Конфигурация логгера
logging.config.fileConfig(celery_config.logging_config)
logger = logging.getLogger(__name__)

# Инициализируем celery
app = Celery(__name__, broker=celery_config.broker, backend=celery_config.backend)
app.config_from_object('etc.celeryconfig')

# Автопоиск задач
app.autodiscover_tasks()


# При запуске celery выполняем
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    celery_type = os.environ.get('CELERY_TYPE')
    if celery_type == 'BEAT':
        # Синхронизация списка интернет ресурсов с базой данных
        logger.info('Start synchronization_db resources list with database')
        try:
            json_resources_list = misc.resources_list_json_dump(resources_list=resources_list)
            result = synchronization_db.task_synchronization_database.apply_async(args=(json_resources_list,),
                                                                                  queue='default')
            ddd = result.get()
            print(ddd)
            print(result.status)

            # Получем список интернет ресурсов для создания запланированных задач

            # Если все впорядке добавляем назначенные задания
            # app.conf.beat_schedule = {
            #     'task_bolid_data_collection': {
            #         'task': 'backend_tasks.v1.tasks.bolid_data_collection',
            #         'schedule': crontab(),
            #         # 'options': {'queue': 'data_collection'}
            #         # 'options': {
            #         #     'routing_key': 'task_data_collection',
            #         #     'priority': 10
            #         # }
            #         # 'args': (16, 16),
            #     },
            # }

            logger.info(f'Celery {celery_type.title()} configuration completed')
        except Exception as error:
            logger.error(error)
            logger.error(traceback.format_exc(limit=None, chain=True))
            logger.warning('Configuration completed with errors')
