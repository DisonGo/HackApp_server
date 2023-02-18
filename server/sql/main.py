from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from sql.models import models
from schemes import dormitory, location, room, university, event
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/locations", response_model=location.LocationCreate)
def post_location(json_location: location.Location, db: Session = Depends(get_db)):
    response = crud.post_location(db=db, loc=json_location)
    return response


@app.post("/rooms", response_model=room.RoomCreate)
def post_room(json_room: room.Room, db: Session = Depends(get_db)):
    response = crud.post_room(db=db, json_room=json_room)
    return response


@app.post("/details", response_model=dormitory.DetailsCreate)
def post_details(detail: dormitory.Details, db: Session = Depends(get_db)):
    response = crud.post_detail(db=db, detail=detail)
    return response


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


@app.post("/dormitories", response_model=dormitory.DormitoryCreate)
def post_dormitory(json_dormitory: dormitory.Dormitory, db: Session = Depends(get_db)):
    response = crud.post_dormitory(db=db, dorm=json_dormitory)
    return response


@app.get("/dormitories", response_model=List[dormitory.DormitoryGet])
def read_dormitories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dormitories = crud.get_dormitories(db, skip=skip, limit=limit)
    return dormitories


@app.post("/universities", response_model=university.UniversityCreate)
def post_dormitory(json_university: university.University, db: Session = Depends(get_db)):
    response = crud.post_university(db=db, json_university=json_university)
    return response


@app.get("/universities", response_model=List[university.UniversityGet])
def read_universities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    universities = crud.get_universities(db, skip=skip, limit=limit)
    return universities


@app.post("/events", response_model=event.EventCreate)
def post_dormitory(json_event: event.Event, db: Session = Depends(get_db)):
    response = crud.post_event(db=db, json_event=json_event)
    return response


@app.get("/events", response_model=List[event.EventGet])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events
