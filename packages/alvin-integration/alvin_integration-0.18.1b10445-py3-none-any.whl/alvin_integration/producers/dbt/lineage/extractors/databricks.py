from dataclasses import dataclass
from datetime import datetime

from alvin_integration.producers.dbt.lineage.extractors.contracts import (
    AlvinAdapterResponse,
)


@dataclass
class AlvinDatabricksAdapterResponse(AlvinAdapterResponse):
    job_id: str = None
    alvin_platform_id: str = None
    event_time: datetime = None
    started: datetime = None
    ended: datetime = None
