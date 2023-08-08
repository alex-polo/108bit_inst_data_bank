from typing import List

from backend_tasks.misc.classes import ResourcesVendor

resources: List[ResourcesVendor] = [
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
