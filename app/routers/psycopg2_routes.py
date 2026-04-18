from fastapi import APIRouter, Response, HTTPException, status
from schemas import Post
from psycopg2_db import cursor, conn

router = APIRouter(prefix="/posts", tags=["psycopg2"])

@router.get("/")
def get_posts():
    cursor.execute("""SELECT * FROM "class" """)
    posts = cursor.fetchall()
    return {"data": posts}


@router.post("/")
def add_student(post: Post):
    cursor.execute("""
        INSERT INTO "class" (roll, first_name, last_name, age)
        VALUES (%s, %s, %s, %s)
        RETURNING *""",
        (post.roll, post.first_name, post.last_name, post.age))

    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@router.get("/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM class WHERE id = %s""", (id,))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=404, detail="Not found")

    return {"post_detail": post}


@router.delete("/{id}", status_code=204)
def delete_post(id: int):
    cursor.execute("""DELETE FROM class WHERE id = %s RETURNING *""", (id,))
    deleted = cursor.fetchone()
    conn.commit()

    if not deleted:
        raise HTTPException(status_code=404, detail="Not found")

    return Response(status_code=204)