from sqlalchemy.orm import Session

from sql.models import models
from sql.schemes import dormitory, room, location, university, event


def post_event(db: Session, json_event: event.Event):
    db_event = models.Event(**json_event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def post_university(db: Session, json_university: university.University):
    db_university = models.University(**json_university.dict())
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    return db_university


def get_universities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.University).offset(skip).limit(limit).all()


def post_room(db: Session, json_room: room.Room):
    db_room = models.Room(**json_room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def post_detail(db: Session, detail: dormitory.Details):
    db_detail = models.DormitoryDetail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail


def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def post_location(db: Session, loc: location.Location):
    db_location = models.Location(**loc.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def get_dormitory(db: Session, dormitory_id: int):
    return db.query(models.Dormitory).filter(models.Dormitory.id == dormitory_id).first()


def get_dormitories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dormitory).offset(skip).limit(limit).all()


def post_dormitory(db: Session, dorm: dormitory.Dormitory):
    db_dormitory = models.Dormitory(**dorm.dict())
    db.add(db_dormitory)
    db.commit()
    db.refresh(db_dormitory)
    return db_dormitory
