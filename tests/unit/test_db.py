import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.storage.repository import product
from app.enums.entity_status import EntityStatus


@pytest.mark.asyncio
async def test_find_product(session_maker: async_sessionmaker[AsyncSession]):
    repo = product.ProductRepository(session_maker)
    items = await repo.find_by_id_in_and_status([1], EntityStatus.ACTIVE.value)
    assert len(items) == 0
