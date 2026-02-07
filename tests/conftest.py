import os
import pytest
from app.storage.db import get_async_engine


@pytest.fixture
def sqlite_engine():
    os.remove("sqlite_test.db") if os.path.exists("sqlite_test.db") else None
    url = "sqlite+aiosqlite:///sqlite_test.db"
    engine = get_async_engine(url, echo=True)
    yield engine
