from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class BaseRepository:
    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self.session_maker = session_maker

    @asynccontextmanager
    async def session_scope(self):
        async with self.session_maker.begin() as session:
            try:
                yield session
                session.commit()
            except Exception:
                await session.rollback()
                raise
