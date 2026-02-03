from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from typing import AsyncGenerator

meta = MetaData()


# engine = create_async_engine("sqlite+aiosqlite://", echo=True)


async def get_session(
    async_session: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with async_session.begin() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
