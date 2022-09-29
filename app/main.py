from app.oauth2 import SECRET_KEY
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)
#the above commented commands is what tell sqlalchemy to create all new tables from the models. But with alembic, it is not neccessary anymore to carry out the step. 

app = FastAPI()
origins = ["*"]
#you can use specific domains like https://www.google.com 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# uvicorn main:app --reload
# uvicorn app.main:app --reload - from a folder

#Heroku setup
#heroku login - first command in the terminal 
#git push heroku main

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello Ajibola!"}



# Alembic code
# alembic init <name_of_the_folder> - creates an alembic folder in the current workspace
# alembic upgrade heads - to upgrade to latest change
# alembic current - to find current stage
# alembic revision -m "message" - to create a revision or state that can be upgraded or reversed
# alembic revision --autogenerate -m "message" - to go through sqlalchemy and autogenerate the changes 
# to make the above work, go env.py in the alembic folder created. then import your Base class from your models, then set the below
#target_metadata = Base.metadata

