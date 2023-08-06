from celery import Celery

from etc import CeleryConfig, get_celery_config

celery_config: CeleryConfig = get_celery_config()

app = Celery(__name__, broker=celery_config.broker, backend=celery_config.backend)
app.config_from_object('etc.celeryconfig')
app.autodiscover_tasks()