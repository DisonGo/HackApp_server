import datetime
from typing import List, Optional
from pydantic import BaseModel


class RoomDetails(BaseModel):
    isFree: bool
    type: str
    price: str
    description: str
    photos: List[str]
    amount: str


class RoomBase(BaseModel):
    details: Optional[RoomDetails] = None
    dormitoryId: Optional[int] = None
    dateFrom: datetime.date
    dateTo: datetime.date
    createdTimestamp: Optional[datetime.date] = None
    onModeration: Optional[bool] = None
    updatedTimestamp: Optional[datetime.date] = None

    class Config:
        orm_mode = True


class Room(RoomBase):
    pass


class RoomCreate(RoomBase):
    id: int
