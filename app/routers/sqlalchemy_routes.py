from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/sqlalchemy", tags=["sqlalchemy"])

@router.get("/")
def test(db: Session = Depends(get_db)):
    return {"message": "SQLAlchemy working"}