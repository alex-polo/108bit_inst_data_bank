import json
from typing import List

from backend_tasks.resources.tools.classes import ResourcesVendor


def resources_list_json_dump(resources_list: List[ResourcesVendor]):
    result_list = list()
    for resource in resources_list:
        result_list.append({
            'system_name': resource.system_name,
            'vendor_name': resource.vendor_name,
            'url': resource.url,
            'vendor_tag': resource.vendor_tag,
            'field_tags': resource.field_tags,
            'is_enabled': resource.is_enabled,
        })

    return json.dumps(result_list)
