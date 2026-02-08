from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

from app.storage import model


def get_engine(url: str, echo: bool = False):
    return create_engine(url, echo=echo)


def get_sessionmaker(engine: Engine):
    return sessionmaker(engine, expire_on_commit=False)


def get_async_engine(url: str, echo: bool = False):
    engine = create_async_engine(url, echo=echo)
    return engine


def get_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False)


async def get_session(
    async_session_maker: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker.begin() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


async def create_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(model.base.Base.metadata.create_all)


async def drop_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(model.base.Base.metadata.drop_all)
