from sqlalchemy.ext.asyncio import AsyncSession
from app.enums.entity_status import EntityStatus
from app.storage.model.product import Product


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_id_in_and_status(
        self, ids: list[int], status: EntityStatus
    ) -> list[Product]:
        query = select(Product).where(Product.id.in_(ids), Product.status == status)
        result = await self.session.execute(query)
        return result.scalars().all()
