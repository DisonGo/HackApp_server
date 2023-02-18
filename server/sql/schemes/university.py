import datetime

from typing import Optional
from pydantic import BaseModel


class Details(BaseModel):
    photo: str
    site: str
    committee: str
    region: str
    shortName: Optional[str] = ""
    founderName: Optional[str] = ""
    district: str


class UniversityBase(BaseModel):
    name: str
    details: Details
    onModeration: bool
    createdTimestamp: datetime.date
    updatedTimestamp: datetime.date


class University(UniversityBase):
    class Config:
        orm_mode = True


class UniversityCreate(University):
    id: int
    pass


class UniversityGet(University):
    pass
