
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases
import os

DATABASE_URL = os.getenv("DATABASE_URL", os.getenv("DATABASE_URL", ""))

database = databases.Database(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def connect_db():
    await database.connect()

async def disconnect_db():
    await database.disconnect()