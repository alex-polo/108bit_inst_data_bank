from dataclasses import dataclass
from typing import List, Any, Optional


@dataclass
class DownloadedContent:
    is_success: bool
    content: Optional[Any]


@dataclass
class ResourcesVendor:
    system_name: str
    vendor_name: str
    url: str
    vendor_tag: str
    field_tags: List[str]
    task: str
    time_execute: str
    is_enabled: bool
