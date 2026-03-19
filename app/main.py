from fastapi import FastAPI, Response , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from find_post import find_post,find_index
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app= FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost' , database = 'mydb' , user = 'postgres' , password = 'password123' , cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected Successfully")
        break
    
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ",error)
        time.sleep(3)


class Post(BaseModel):
    title: str
    content : str
    publish : bool = True
    rating : Optional[int] = None

my_posts=[{"title":"Title of post","content" : "Content Of Post", "id" : 1},
                    {"title":"Title of post","content" : "Content Of Post", "id" : 2},
                    {"title":"Title of post","content" : "Content Of Post", "id" : 3},
                    {"title":"Puja","content" : "Goofy me", "id" : 4},
                    {"title" : "Prava", "content" : "Dashian 2082" , "id" : 5}]


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
def get_post(id : int , response : Response):
    post = find_post(id,my_posts)
    if not post:
        response.status_code = 404
        return {"detail" : f"Post with id no. {id} was not found"}
    return {"post_detail" : post}

@app.delete("/posts/delete/{id}" , status_code=204)
def delete_post(id : int):
    index = find_index(id,my_posts)

    if index == None:
        raise HTTPException(status_code=404, detail=f"Post with id no: {id} doesnt exist")

    my_posts.pop(index)
    return Response(status_code=204)



@app.put("/posts/{id}")
def update_post(id : int , post : Post):
    index = find_index(id,my_posts)

    if index == None:
        raise HTTPException(status_code=404, detail=f"Post with id no: {id} doesnt exist")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    print(post_dict)
    return{"data" : post_dict}

    
    
    
