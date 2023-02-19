from typing import List
from pydantic import BaseModel


class Coordinates(BaseModel):
    lat: float
    lng: float


class LocationBase(BaseModel):
    name: str
    city: str
    street: str
    mealPlan: str
    coordinates: Coordinates
    houseNumber: str
    minDays: str
    maxDays: str
    photos: List[str]

    class Config:
        orm_mode = True


class Location(LocationBase):
    pass


class LocationCreate(LocationBase):
    id: int


class LocationGet(LocationCreate):
    pass
