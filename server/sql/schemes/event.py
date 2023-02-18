import datetime
from typing import List, Optional
from pydantic import BaseModel

class Details(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    video: Optional[List[str]] = None
    photos: Optional[List[str]] = None
    type: Optional[str] = None
    WoS: Optional[str] = None

class EventBase(BaseModel):
    dateFrom: datetime.date
    dateTo: datetime.date
    details: Details
    userId: Optional[int] = None
    universityId: Optional[int] = None
    onModeration: bool
    createdTimestamp: datetime.date
    updatedTimestamp: datetime.date


class Event(EventBase):

    class Config:
        orm_mode = True


class EventCreate(Event):
    id: int
    pass


class EventGet(Event):
    pass
