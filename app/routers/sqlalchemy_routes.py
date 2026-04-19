from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import Student

router = APIRouter(prefix="/sqlalchemy", tags=["sqlalchemy"])

@router.get("/posts")
def get_all(db : Session = Depends(get_db)):
    posts = db.query(models.Student).all()
    return {"data" : posts}

@router.post("/posts")
def add_student(student : Student , db : Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"data" : new_student}