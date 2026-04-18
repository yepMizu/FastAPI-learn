from fastapi import FastAPI
from routers import psycopg2_routes, sqlalchemy_routes
from database import engine, Base
import models 

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(psycopg2_routes.router)
app.include_router(sqlalchemy_routes.router)