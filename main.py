from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app= FastAPI()

class Post(BaseModel):
    title: str
    content : str
    publish : bool = True
    rating : Optional[int] = None

my_posts=[{"title":"Title of post","content" : "Content Of Post", "id" : "1"},
                    {"title":"Title of post","content" : "Content Of Post", "id" : "2"},
                    {"title":"Title of post","content" : "Content Of Post", "id" : "3"},]


@app.get("/posts")
async def root():
    return{"data": my_posts}



@app.post("/posts")
async def get_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,100000)
    my_posts.append(post_dict)
    return{"data" : post_dict}


@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"data" : f"This is post no.{id}"}

    
