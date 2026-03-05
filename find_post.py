from fastapi import FastAPI

def find_post(id,my_posts):
    for p in my_posts:
        if p["id"] == id:
            return p
    return None

