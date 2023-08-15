set CELERY_TYPE=WORKER
venv\Scripts\celery.exe -A backend_tasks.main:app worker --pool=solo --hostname=data_bank@%hostname%