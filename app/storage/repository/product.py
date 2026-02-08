import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from app.enums.entity_status import EntityStatus
from app.storage.model.product import Product


class ProductRepository:
    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self.session_maker = session_maker

    async def save(self, product: Product):
        async with self.session_maker.begin() as session:
            session.add(product)
            session.commit()

    async def find_by_id_in_and_status(
        self, ids: list[int], status: EntityStatus
    ) -> list[Product]:
        async with self.session_maker.begin() as session:
            query = sa.select(Product).where(
                Product.id.in_(ids), Product.status == status
            )
            result = await session.execute(query)
            return result.scalars().all()
