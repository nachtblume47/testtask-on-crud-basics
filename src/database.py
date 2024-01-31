
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import DB_NAME, DB_PORT, DB_ADDR, DB_USER, DB_PASS
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


engine = create_async_engine(DB_URL)
async_session = async_sessionmaker(engine, expire_on_commit=True)




