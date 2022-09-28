from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLAlchemy_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLAlchemy_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database='fastapi',
#                                 user='postgres', password='Life&joy1', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfully created")
#         break
#     except Exception as e:
#         print("Connecting to Database failed")
#         print(f"Error was {e}")
#         time.sleep(2)
