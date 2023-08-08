from typing import List

import backend_tasks
from backend_tasks import v1 as tasks_v1
from resources.tools.classes import ResourcesVendor

resources_list: List[ResourcesVendor] = [
    ResourcesVendor(
        system_name='bolid',
        vendor_name='bolid',
        url='https://bolid.ru/',
        vendor_tag='#Bolid',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        task='backend_tasks.bolid_data_collection',
        time_execute='1',
        is_enabled=True
    )
]