import os
import pytest
import asyncio
from app.storage import db
from app.storage.repository import product


@pytest.fixture(scope="session")
def sqlite_engine():
    DB_FILE = "sqlite_test.db"
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    url = f"sqlite+aiosqlite:///{DB_FILE}"
    engine = db.get_async_engine(url, echo=True)
    asyncio.run(db.create_tables(engine))
    yield engine
    asyncio.run(db.drop_tables(engine))


@pytest.fixture(scope="function")
def sqlite_session_maker(sqlite_engine):
    yield db.get_session_maker(sqlite_engine)


@pytest.fixture(scope="function")
def sqlite_product_repository(sqlite_session_maker):
    return product.ProductRepository(sqlite_session_maker)
