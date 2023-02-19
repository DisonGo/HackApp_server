from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from sql.models import models
from schemes import dormitory, location, room, university, event
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/locations", response_model=List[location.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations


@app.get("/locations/{location_id}", response_model=location.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@app.get("/dormitories", response_model=List[dormitory.DormitoryGet])
def read_dormitories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dormitories = crud.get_dormitories(db, skip=skip, limit=limit)
    return dormitories


@app.get("/universities", response_model=List[university.UniversityGet])
def read_universities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    universities = crud.get_universities(db, skip=skip, limit=limit)
    return universities


@app.get("/events", response_model=List[event.EventGet])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events
