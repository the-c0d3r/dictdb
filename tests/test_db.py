import pytest

from lib.db import Database


@pytest.fixture
def db() -> Database:
    database = Database("/tmp/db.json")
    database.purge()
    return database


class TestDatabase:
    def test_init(self, db):
        assert db is not None

        with pytest.raises(Exception) as exec_info:
            db = Database("/usr/bin/db.json")
        assert "not permitted" in str(exec_info.value)

    def test_count(self, db):
        assert db.count() == 0

        db.insert({"word": "test", "definition": "test abc"})
        assert db.count() == 1

    def test_insert(self, db):
        assert db.insert(42) == False
        assert db.insert({"word": "test", "definition": "test"}) == True

    def test_query(self, db):
        db.insert({"word": "test", "definition": "test abc"})
        result = db.query("test")
        assert result is not None
        assert result[0].get("word") == "test"
        assert result[0].get("definition") == "test abc"

        result = db.query("NOSUCHWORD")
        assert result == []

    def test_update(self, db):
        db.insert({"word": "test", "definition": "test abc"})
        db.insert({"word": "abc", "definition": "def"})
        db.update({"word": "test", "definition": "new def"})

        result = db.query("test")[0]
        assert result.get("definition") == "new def"

    def test_all(self, db):
        db.insert({"word": "test", "definition": "test abc"})
        results = db.all()

        assert len(results) == 1
        assert db.count() == 1
        assert results[0].get("word") == "test"

    def test_delete(self, db):
        db.insert({"word": "test", "definition": "test abc"})
        db.delete("test")

        assert db.count() == 0
        assert len(db.all()) == 0

    def test_purge(self, db):
        db.insert({"word": "test", "definition": "test abc"})
        db.purge()

        assert len(db.all()) == 0
        assert db.count() == 0
