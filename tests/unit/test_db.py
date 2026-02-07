import pytest
from sqlalchemy.ext.asyncio import AsyncEngine

from app.storage import db


@pytest.mark.asyncio
async def test_create_tables(sqlite_engine: AsyncEngine):
    await db.create_tables(sqlite_engine)
