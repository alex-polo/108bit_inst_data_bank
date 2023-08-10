import json
from typing import List

from backend_tasks.misc.classes import ResourcesVendor


def serialize_resource(resources: List[ResourcesVendor]):
    return json.dumps(resources)


def deserialize_resource(serialized_data):
    print(serialized_data)
    data = json.loads(serialized_data)
    return ResourcesVendor(name=data['name'])
