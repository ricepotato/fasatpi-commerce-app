from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text

from app.storage.model.base import BaseModel


class Product(BaseModel):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(255))
    thumbnail_url: Mapped[str] = mapped_column(String(500))
    description: Mapped[str] = mapped_column(Text)
    short_description: Mapped[str] = mapped_column(Text)
    cost_price: Mapped[int] = mapped_column(Integer)
    sales_price: Mapped[int] = mapped_column(Integer)
    discount_price: Mapped[int] = mapped_column(Integer)
