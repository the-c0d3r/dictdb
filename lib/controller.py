import os
from argparse import Namespace
from typing import Optional, Dict

import editor

from lib.db import Database
from lib.entry import Entry


class Controller:
    """Class to control the dictdb"""

    def __init__(self, args: Namespace) -> None:
        self._db = Database()

        if args.add:
            self.add(args.add)

        if args.search:
            self.search(args.search)

        if args.interactive:
            self.interactive()

        if args.list:
            self.list()

        if args.edit:
            self.edit(args.edit)

        if args.delete:
            self.delete(args.delete)

        if args.load:
            self.load(args.load)

    def interactive(self) -> None:
        """
        Launch editor with all the entries
        """
        # load all the entries into editor
        entries = self._db.all()
        lines = []
        for line in entries:
            entry = Entry(line)
            lines.append(entry.get_str())

        raw = editor.edit(contents = "\n".join(lines))

        # update all the entries from editor to db
        lines = [line.strip("\n") for line in raw.decode().strip().split("\n")]
        # purge db and overwrite with current copy
        self._db.purge()

        for line in lines:
            entry = Entry(line)
            if entry.is_valid():
                self._db.insert(entry.get_dict())

    def load(self, filename: str) -> None:
        """
        import the custom dictionary file to database
        :param filename: the filename to import
        """
        if not os.path.exists(filename):
            print("Error: file not found")
            return
        # todo: read the file, strip '\n' and parse into entry, add to db
        with open(filename, "r") as fp:
            content = [line.strip("\n") for line in fp.readlines()]

        print(f"[+] Loaded {len(content)} lines")

        imported = 0
        for line in content:
            entry = Entry(line)
            if entry.is_valid():
                self._db.insert(entry.get_dict())
                imported += 1

        print(f"[+] Imported {imported} entries")
        print(f"[+] Dictionary size : {self._db.count()}")

    def list(self) -> None:
        """list all the entries in the database"""
        words = self._db.all()
        if not words:
            print("[-] No words found in the database")
            return

        entries = [self.dict2entry(word) for word in words]
        for entry in entries:
            print(entry.get_str())

    def add(self, data: str) -> None:
        entry = Entry(data)
        if not entry.is_valid():
            # means parsing failed
            print("--add requires the data in the following format")
            print("--add 'word : (type) definition'")
            exit()
        self._db.insert(entry.get_dict())

    def search(self, data: str) -> None:
        results = self._db.query(data)

        if not results:
            print("Unable to find word in db")
            return

        for result in results:
            word = result.get("word")
            definition = result.get("definition")

            print("Word       : ", word)
            print("Definition : ", definition)
            print("\n")

    def delete(self, data: str) -> None:
        """Function to delete the entry"""
        results = self._db.query(data)

        if not results:
            print("Unable to find word in db")
            return

        return self._db.delete(data)

    def edit(self, data: str) -> None:
        """Function to modify the existing definitions"""
        # BUG: this function seem to overwrite the existing entries and create two copies
        results = self._db.query(data)

        if not results:
            print("Unable to find word in db")
            return

        if len(results) > 1:
            print(f"Multiple results found for {data}, please retry with exact word")
            return self.search(data)

        word = results[0].get("word")
        definition = results[0].get("definition")

        # acquire the new content from the editor
        raw = editor.edit(contents = f"{word}: {definition}")

        entry = Entry(raw.decode().strip())
        if not entry.is_valid():
            print("Unable to parse the edited content, it must be in the following format, type is optional")
            print("word : (type) definition")
            return
        self._db.update(entry.get_dict())

    def dict2entry(self, data: dict) -> Optional[Entry]:
        word = data.get("word")
        definition = data.get("definition")

        if word and definition:
            return Entry(f"{word} : {definition}")

        return None

    def entry2dict(self, entry: Entry) -> Optional[Dict]:
        if entry.is_valid():
            return entry.get_dict()
        return None
