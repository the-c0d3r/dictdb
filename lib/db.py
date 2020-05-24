import os
from typing import Dict, Optional, List

import tinydb


class Database:
    """
    This class is to handle all database related operations
    """

    def __init__(self, filename: str = None) -> None:
        if filename:
            self.filename = filename
        else:
            self.filename = os.path.dirname(os.path.dirname(__file__)) + os.path.sep + "data/database.json"

        # Create the file if not found
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()
        self.db = tinydb.TinyDB(self.filename)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.db.close()

    def count(self) -> int:
        """ Returns the number of record in the Database """
        return len(self.db.all())

    def insert(self, data: Dict) -> bool:
        """
        :param data: the data to write to database
        data would be a dictionary object to write into the class

        Designated data format as follows, e.g.
        {'word': 'example', 'definition' : 'be illustrated'}
        """
        if not isinstance(data, dict) or not data.get("word") or not data.get("definition"):
            return False

        self.db.insert(data)
        return True

    def query(self, data: str) -> Optional[Dict]:
        """
        :param data: a query expression for the database
        :returns : a dictionary/json object for the matching result
        """
        query = tinydb.Query()
        return self.db.search(query.word.matches(data))

    def all(self) -> Optional[List[Dict]]:
        """return all entries from the db"""
        return self.db.all()

    def update(self, entry: Dict) -> None:
        """updates the entry in the database"""
        query = tinydb.Query()
        self.db.upsert(entry, query.word == entry.get("word"))

    def delete(self, data: str) -> None:
        """deletes the data from the database"""
        self.db.remove(tinydb.Query().word == data)

    def purge(self) -> None:
        """removes the entire db"""
        self.db.drop_tables()
