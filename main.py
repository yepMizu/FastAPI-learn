from fastapi import FastAPI
from fastapi.params import Body

app= FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello World 222"}

@app.get("/posts")
async def get_post():
    return{"data":"This is a post"}

@app.post("/createpost")
async def get_post(body: dict =Body(...)):
    return{"new_post":f"title--> {body["title"]} content-->{body["content"]}"}
