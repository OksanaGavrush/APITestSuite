from typing import Optional
from pydantic import BaseModel, Field


class PublicationData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')
    color: Optional[str] = None


class Publication(BaseModel):
    id: str
    name: str
    data: PublicationData
    updatedAt: str
