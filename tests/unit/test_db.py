import pytest

from app.storage.repository import product
from app.enums.entity_status import EntityStatus


@pytest.mark.asyncio
async def test_find_product(sqlite_product_repository: product.ProductRepository):
    items = await sqlite_product_repository.find_by_id_in_and_status(
        [1], EntityStatus.ACTIVE.value
    )
    assert len(items) == 0


@pytest.mark.asyncio
async def test_save_product(sqlite_product_repository: product.ProductRepository):
    new_product = product.Product(
        name="Test Product",
        description="A product for testing",
        cost_price=100,
    )
    await sqlite_product_repository.save(new_product)

    items = await sqlite_product_repository.find_by_id_in_and_status(
        [new_product.id], EntityStatus.ACTIVE.value
    )
    assert len(items) == 1
    assert items[0].name == "Test Product"
