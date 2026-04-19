
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from database import Base



class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, nullable = False, primary_key = True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    age = Column(Integer, nullable = False)
    is_passed = Column(Boolean, nullable = False)
    joined_at = Column(TIMESTAMP(timezone = True), nullable = False , server_default = text('now()'))

