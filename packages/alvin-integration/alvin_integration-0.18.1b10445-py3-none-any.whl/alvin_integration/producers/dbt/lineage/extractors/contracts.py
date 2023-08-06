from dataclasses import dataclass
from datetime import datetime

from dbt.contracts.connection import AdapterResponse


@dataclass
class AlvinAdapterResponse(AdapterResponse):
    job_id: str = None
    alvin_platform_id: str = None
    event_time: datetime = None
    started: datetime = None
    ended: datetime = None
