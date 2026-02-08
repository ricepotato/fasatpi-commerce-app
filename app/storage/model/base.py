import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declared_attr

from app.enums.entity_status import EntityStatus


class Base(DeclarativeBase):
    pass


class BaseModelMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {"mysql_engine": "InnoDB"}
    __mapper_args__ = {"always_refresh": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(
        String(20), default=EntityStatus.ACTIVE.value, index=True
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    deleted_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now
    )

    def active(self):
        self.status = EntityStatus.ACTIVE.value

    def is_active(self):
        return self.status == EntityStatus.ACTIVE.value

    def delete(self):
        self.deleted_at = datetime.datetime.now()
        self.status = EntityStatus.DELETED.value

    def is_deleted(self):
        return self.status == EntityStatus.DELETED.value
