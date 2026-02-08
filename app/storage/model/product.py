from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text

from app.storage.model import base


class Product(base.Base, base.BaseModelMixin):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    thumbnail_url: Mapped[str] = mapped_column(String(500), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    short_description: Mapped[str] = mapped_column(Text, nullable=True)
    cost_price: Mapped[int] = mapped_column(Integer, nullable=False)
    sales_price: Mapped[int] = mapped_column(Integer, nullable=True)
    discount_price: Mapped[int] = mapped_column(Integer, nullable=True)
