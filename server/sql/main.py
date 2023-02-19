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
    db_locations = crud.get_locations(db, skip=skip, limit=limit)
    if db_locations is None:
        raise HTTPException(status_code=404, detail="Locations not found")
    return db_locations


@app.get("/locations/{location_id}", response_model=location.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@app.get("/dormitories", response_model=List[dormitory.DormitoryGet])
def read_dormitories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_dormitories = crud.get_dormitories(db, skip=skip, limit=limit)
    if db_dormitories is None:
        raise HTTPException(status_code=404, detail="Dormitories not found")
    return db_dormitories


@app.get("/dormitories/{dormitory_id}", response_model=dormitory.DormitoryGet)
def read_dormitory(dormitory_id: int, db: Session = Depends(get_db)):
    db_dormitory = crud.get_dormitory(db, dormitory_id=dormitory_id)
    if db_dormitory is None:
        raise HTTPException(status_code=404, detail="Dormitory not found")
    return db_dormitory


@app.get("/universities", response_model=List[university.UniversityGet])
def read_universities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_universities = crud.get_universities(db, skip=skip, limit=limit)
    if db_universities is None:
        raise HTTPException(status_code=404, detail="Universities not found")
    return db_universities


@app.get("/universities/{university_id}", response_model=university.University)
def read_university(university_id: int, db: Session = Depends(get_db)):
    db_university = crud.get_university(db, university_id=university_id)
    if db_university is None:
        raise HTTPException(status_code=404, detail="University not found")
    return db_university


@app.get("/events", response_model=List[event.EventGet])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_events = crud.get_events(db, skip=skip, limit=limit)
    if db_events is None:
        raise HTTPException(status_code=404, detail="Events not found")
    return db_events


@app.get("/events/{event_id}", response_model=event.Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
