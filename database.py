from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import  Column, Integer, String
from typing import Optional

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///tasks.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class Tasks(Model):
    __tablename__ = "Tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)








