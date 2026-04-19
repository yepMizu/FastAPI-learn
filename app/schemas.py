from pydantic import BaseModel

class Post(BaseModel):
    roll : int 
    first_name : str
    last_name : str
    age : int
    

class Student(BaseModel):
    first_name : str
    last_name : str
    age : int 
    is_passed : bool

