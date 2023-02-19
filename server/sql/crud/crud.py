from sqlalchemy.orm import Session

from sql.models import models

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def get_university(db: Session, university_id: int):
    return db.query(models.University).filter(models.University.id == university_id).first()


def get_universities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.University).offset(skip).limit(limit).all()


def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def get_dormitory(db: Session, dormitory_id: int):
    return db.query(models.Dormitory).filter(models.Dormitory.id == dormitory_id).first()


def get_dormitories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dormitory).offset(skip).limit(limit).all()
