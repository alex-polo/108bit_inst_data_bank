from typing import List

from backend_tasks.resources.parsers import bolid
from backend_tasks.resources.tools.classes import ResourcesVendor

resources_list: List[ResourcesVendor] = [
    ResourcesVendor(
        system_name='bolid',
        vendor_name='bolid',
        url='https://bolid.ru/',
        vendor_tag='#Bolid',
        field_tags=['#Системы_автоматики', '#Системы_безопасности'],
        parser_function=bolid.parse_resource,
        is_enabled=True
    )
]