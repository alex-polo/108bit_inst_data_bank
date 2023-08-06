from celery import shared_task


@shared_task()
def add(x, y):
    import requests
    answer = requests.get('https://bolid.ru/support/download/?groupsID=4')
    print(answer)


@shared_task()
def bolid_data_collection() -> None:
    import requests
    answer = requests.get('https://bolid.ru/support/download/?groupsID=4')
    print(answer)
