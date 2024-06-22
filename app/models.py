from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Dataset:
    org_id: str
    id: str
    name: str
    type: str

@dataclass
class Data:
    dataset_id: str
    id: str
    value: str


@dataclass
class ViolationReport:
    dataset_id: str
    violation_type: str
    description: str
    multimedia_type: str  # 'text', 'image', 'audio', 'video', or 'animation'
    content_identifier: str  # This could be a file name, URL, or database ID
    data_id: Optional[str] = None
    location: Optional[str] = None  # This could be used for timestamp in video/audio or coordinates in image