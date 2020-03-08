import os
import logging

from typing import Dict, Optional, List
import tinydb


class Database:
    """
    This class is to handle all database related operations
    """
    def __init__(self):
        self.filename = os.path.dirname(os.path.dirname(__file__)) + os.path.sep + "data/database.json"
        self.db = tinydb.TinyDB(self.filename)

    def get_count(self) -> int:
        """ Returns the number of record in the Database """
        return len(self.db.all())

    def insert(self, data: Dict) -> bool:
        """
        :param data: the data to write to database
        data would be a dictionary object to write into the class

        Designated data format as follows
        {'word': { 'definition' : 'a word', 'type' : 'noun' } }
           ^                          ^                 ^
           |                          |                 |
        the dictionary entry          |                 |
                                the definition          |
                                                type of word aka noun, verb
        """
        try:
            self.db.insert(data)
        except Exception:
            return False
        else:
            return True

    def query(self, data: str) -> Optional[Dict]:
        """
        :param data: a query expression for the database
        :returns : a dictionary/json object for the matching result
        """
        query = tinydb.Query()
        return self.db.search(query.word.matches(data))

    def get(self, data: str) -> Optional[tinydb.database.Document]:
        """Returns the document object"""
        return self.db.get(tinydb.Query().word == data)

    def all(self) -> Optional[List[Dict]]:
        """return all entries from the db"""
        return self.db.all()

    def update(self, entry: Dict) -> None:
        """updates the entry in the database"""
        self.db.update(entry.get_data())

    def delete(self, data: str) -> None:
        """deletes the data from the database"""
        self.db.remove(tinydb.Query().word == data)

    def purge(self) -> None:
        """removes the entire db"""
        self.db.purge()

