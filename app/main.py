from fastapi import FastAPI, Response , HTTPException, status
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
        conn = psycopg2.connect(host='localhost' , database = 'MyDB' , user = 'postgres' , password = 'password123' , cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected Successfully")
        break
    
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ",error)
        time.sleep(3)



class Post(BaseModel):
    roll : int 
    first_name : str
    last_name : str
    age : int
    
@app.get("/posts")
async def root():
    cursor.execute("""SELECT * FROM "class" """)
    posts = cursor.fetchall()
    print(posts)
    return{"data" : posts}
    
@app.post("/posts")
def add_student(post: Post):
    cursor.execute("""
        INSERT INTO "class" (roll, first_name, last_name, age)
        VALUES (%s, %s, %s, %s)
        RETURNING *""", 
        (post.roll, post.first_name, post.last_name, post.age)) 

    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id : int , response : Response):
    cursor.execute(""" SELECT * from class WHERE id = %s """, (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with id: {id} not found")
    return {"post_detail" : post}

@app.delete("/posts/delete/{id}" , status_code=204)
def delete_post(id : int):
    cursor.execute(""" DELETE FROM class WHERE id = %s RETURNING * """ , (id,))
    delete_post = cursor.fetchone()
    conn.commit()

    if not delete_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id no: {id} doesnt exist")
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

    
    
    
