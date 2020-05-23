import pytest

from lib.entry import Entry


@pytest.fixture
def entry():
    return Entry("test: word definition")


class TestEntry:
    def test_init(self, entry):
        assert entry is not None

    def test_get_data(self, entry):
        data = entry.get_data()
        assert data.get("word") == "test"
        assert data.get("definition") == "word definition"

    def test_valid(self, entry):
        assert entry.is_valid()

    def test_str(self, entry):
        assert entry.str() == "test: word definition"
