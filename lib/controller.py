from argparse import Namespace
from typing import Optional, Dict

import editor

from lib.db import Database
from lib.entry import Entry


class Controller:
    """Class to control the dictdb"""

    def __init__(self) -> None:
        """Initialize the controller"""
        self.db = Database()

    def interact(self, args: Namespace) -> None:
        """start the interaction with the database"""
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

    def interactive(self) -> None:
        """
        Launch editor with all the entries
        """
        # load all the entries into editor
        entries = self.db.all()
        lines = []
        for line in entries:
            entry = self.dict2entry(line)
            lines.append(entry.get_str())

        raw = editor.edit(contents = "\n".join(lines))

        # update all the entries from editor to db
        lines = [line.strip("\n") for line in raw.decode().strip().split("\n")]
        # purge db and overwrite with current copy
        self.db.purge()

        for line in lines:
            entry = Entry(line)
            if entry.is_valid():
                self.db.insert(entry.get_dict())

    def load_content(self, content: [str]) -> None:
        """load the given content"""
        self.db.purge()
        if len(content) == 0:
            print("[-] Nothing to load")
            return

        print(f"[+] Loaded {len(content)} lines")

        imported = 0
        for line in content:
            entry = Entry(line)
            if entry.is_valid():
                self.db.insert(entry.get_dict())
                imported += 1

        print(f"[+] Imported {imported} entries")
        print(f"[+] Dictionary size : {self.db.count()}")

    def list(self) -> None:
        """list all the entries in the database"""
        words = self.db.all()
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
        self.db.insert(entry.get_dict())

    def search(self, data: str) -> None:
        results = self.db.query(data)

        if not results:
            print("[-] Unable to find word in db")
            return

        for result in results:
            entry = self.dict2entry(result)
            print(entry.get_str())

    def delete(self, data: str) -> None:
        """Function to delete the entry"""
        results = self.db.query(data)

        if not results:
            print("Unable to find word in db")
            return

        return self.db.delete(data)

    def edit(self, data: str) -> None:
        """
        Function to modify the existing definitions
        If there are multiple word matches, all of them will be present in the editor
        If there is no match, empty editor will launch, and allow you to save new entry
        """
        results = self.db.query(data)

        content = []
        for word in results:
            entry = self.dict2entry(word)
            content.append(entry.get_str())

        # Launch editor with the matched entries
        raw = editor.edit(contents = "\n".join(content))

        # acquire the new content from the editor
        content = raw.decode().strip().split("\n")

        # Update existing entries or insert new entry
        for line in content:
            entry = Entry(line)
            if not entry.is_valid():
                print(f"[-] Unable to parse the line: '{line}'")
                print("[-] word : (type) definition")
            else:
                self.db.update(entry.get_dict())

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
