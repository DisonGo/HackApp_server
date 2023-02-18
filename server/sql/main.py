from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
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


@app.post("/locations/", response_model=schemas.LocationCreate)
def post_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    response = crud.post_location(db=db, location=location)
    return response


@app.get("/locations/", response_model=List[schemas.Location])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations


@app.get("/locations/{location_id}", response_model=schemas.Location)
def read_user(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location
