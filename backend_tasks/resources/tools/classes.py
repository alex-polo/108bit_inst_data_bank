from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass
class ResourcesVendor:
    system_name: str
    vendor_name: str
    url: str
    vendor_tag: str
    field_tags: List[str]
    parser_function: Optional[Any]
    is_enabled: bool
