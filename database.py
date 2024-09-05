from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "Task"
    id: Column(Integer, primery_key=True, index=True)
    name: Column(String)
    task: Column(String)

Base.metadata.create_all(bind=engine)








