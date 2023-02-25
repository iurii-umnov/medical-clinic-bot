from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.data.config import DB_URL

Base = declarative_base()

async_engine = create_async_engine(DB_URL, echo=False)

AsyncLocalSession = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)
