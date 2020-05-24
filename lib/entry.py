import re
from typing import Dict


class Entry:
    """Dictionary Entry object"""
    pattern = re.compile(r"([^:]*)\s?:\s?(.+)")

    def __init__(self, data: str) -> None:
        """
        Initialize the entry object
        :param data: string in the following format
        word : meaning
        """
        try:
            [[word, definition]] = self.pattern.findall(data)
        except ValueError:
            # means parsing failed
            self._word = ""
            self._definition = ""
        else:
            self._word = word.strip()
            self._definition = definition.strip()

    def is_valid(self) -> bool:
        return self._word != "" and self._definition != ""

    @property
    def word(self) -> str:
        return self._word

    @property
    def definition(self) -> str:
        return self._definition

    def get_dict(self) -> Dict:
        """convert entry into dict data format for db insertion"""
        return {
            'word'      : self._word,
            'definition': self._definition
        }

    def get_str(self) -> str:
        """convert the entry into printable readable string"""
        return self.str()

    def str(self) -> str:
        """return str"""
        return f"{self._word} : {self._definition}"
