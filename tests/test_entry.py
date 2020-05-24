import pytest

from lib.entry import Entry


@pytest.fixture
def entry():
    return Entry("test: word definition")


class TestEntry:
    def test_init(self):
        entry = Entry("test : abcdef")
        assert entry.is_valid()

        entry = Entry("test:abcdef")
        assert entry.is_valid()
        assert entry.word == "test"
        assert entry.definition == "abcdef"

        entry = Entry("test :abcdef")
        assert entry.is_valid()
        assert entry.word == "test"
        assert entry.definition == "abcdef"

        entry = Entry("test: abcdef")
        assert entry.is_valid()
        assert entry.word == "test"
        assert entry.definition == "abcdef"

        entry = Entry("test")
        assert not entry.is_valid()

    def test_phrase(self):
        entry = Entry("zero sum: 0")
        assert entry.is_valid()

        assert entry.word == "zero sum"
        assert entry.definition == "0"

    def test_props(self, entry):
        assert entry.word == "test"
        assert entry.definition == "word definition"

    def test_get_data(self, entry):
        data = entry.get_dict()
        assert data.get("word") == "test"
        assert data.get("definition") == "word definition"

    def test_valid(self, entry):
        assert entry.is_valid()

    def test_str(self, entry):
        assert entry.str() == "test: word definition"
