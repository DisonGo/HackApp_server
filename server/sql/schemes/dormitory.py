import datetime
from typing import List, Optional
from pydantic import BaseModel
from sql.schemes.location import Location


class Service(BaseModel):
    isFree: bool
    name: str
    description: str
    price: str


class Committee(BaseModel):
    email: str
    phone: str
    name: str


class Rules(BaseModel):
    requiredUniDocuments: str
    requiredStudentsDocuments: str
    committee: Committee


class DetailsBase(BaseModel):
    dormitoryId: Optional[int] = None
    locationId: Optional[int] = None
    services: Optional[List[Service]] = None
    rules: Optional[Rules] = None
    documents: Optional[List[str]] = None


class Details(DetailsBase):


    class Config:
        orm_mode = True


class DetailsCreate(Details):
    id: int
    location: Location

class DetailsGet(DetailsCreate):
    pass
class DormitoryBase(BaseModel):
    userId: Optional[int] = None
    universityId: Optional[int] = None
    detailId: Optional[int] = None
    onModeration: Optional[bool] = False
    createdTimestamp: datetime.date
    updatedTimestamp: datetime.date

    class Config:
        orm_mode = True


class Dormitory(DormitoryBase):
    pass


class DormitoryCreate(DormitoryBase):
    id: int


class DormitoryGet(DormitoryCreate):
    details: Optional[Details] = None

