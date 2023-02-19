from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship

from ..database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    dateFrom = Column(Date)
    dateTo = Column(Date)
    details = Column(JSON)
    userId = Column(Integer, ForeignKey("users.id"), nullable=True)
    universityId = Column(Integer, ForeignKey("universities.id"), nullable=True)
    onModeration = Column(Boolean, default=False)
    createdTimestamp = Column(Date)
    updatedTimestamp = Column(Date)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)


class University(Base):
    __tablename__ = "universities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(JSON)
    onModeration = Column(Boolean, default=True)
    createdTimestamp = Column(Date)
    updatedTimestamp = Column(Date)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    street = Column(String)
    mealPlan = Column(String)
    coordinates = Column(JSON)
    houseNumber = Column(String)
    minDays = Column(Integer)
    maxDays = Column(Integer)
    photos = Column(JSON, nullable=True)


class Dormitory(Base):
    __tablename__ = "dormitories"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(ForeignKey("users.id"))
    universityId = Column(ForeignKey("universities.id"))
    detailId = Column(ForeignKey("dormitories_detail.id"), nullable=True)
    details = relationship("DormitoryDetail", foreign_keys=[detailId])
    createdTimestamp = Column(Date)
    updatedTimestamp = Column(Date)
    onModeration = Column(Boolean, default=False)
    rooms = relationship("Room")


class DormitoryDetail(Base):
    __tablename__ = "dormitories_detail"
    id = Column(Integer, primary_key=True, index=True)
    dormitoryId = Column(ForeignKey("dormitories.id"))
    locationId = Column(ForeignKey("locations.id"))
    location = relationship("Location")
    services = Column(JSON, nullable=True)
    rules = Column(JSON, nullable=True)
    documents = Column(JSON, nullable=True)


class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    details = Column(JSON)
    dateFrom = Column(Date)
    dateTo = Column(Date)
    dormitoryId = Column(ForeignKey("dormitories.id"))
    userId = Column(ForeignKey("users.id"))
    universitiesId = Column(ForeignKey("universities.id"))
    createdTimestamp = Column(Date)
    updatedTimestamp = Column(Date)
    onModeration = Column(Boolean, default=True)
