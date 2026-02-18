from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app= FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello World 222"}

class Post(BaseModel):
    title: str
    content : str
    publish : bool = True
    rating : Optional[int] = None

@app.post("/createpost")
async def get_post(new_post: Post):
    print(new_post.rating)
    return{"Info":"New Post created.."}
