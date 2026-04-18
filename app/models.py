
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, nullable = False, primary_key = True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    age = Column(Integer, nullable = False)
    is_passed = Column(Boolean, nullable = False)

