import os
import pytest
from app.storage.db import get_async_engine


@pytest.fixture
def sqlite_engine():
    DB_FILE = "sqlite_test.db"
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    url = f"sqlite+aiosqlite:///{DB_FILE}"
    yield get_async_engine(url, echo=True)
