import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.enums.entity_status import EntityStatus


class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default=EntityStatus.ACTIVE.value)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )

    def active(self):
        self.status = EntityStatus.ACTIVE.value

    def is_active(self):
        return self.status == EntityStatus.ACTIVE.value

    def delete(self):
        self.status = EntityStatus.DELETED.value

    def is_deleted(self):
        return self.status == EntityStatus.DELETED.value


class Product(BaseModel):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(255))
    thumbnail_url: Mapped[str] = mapped_column(String(500))
    description: Mapped[str] = mapped_column(Text)
    short_description: Mapped[str] = mapped_column(Text)
    cost_price: Mapped[int] = mapped_column(Integer)
    sales_price: Mapped[int] = mapped_column(Integer)
    discount_price: Mapped[int] = mapped_column(Integer)
