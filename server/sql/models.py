from sqlalchemy import Column, Integer, String, JSON, ARRAY

from database import Base


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
