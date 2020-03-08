#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from typing import Dict


class Entry:
    """Dictionary Entry object"""
    pattern = re.compile(r"(\S+):\s?(.+)")

    def __init__(self, data: str) -> None:
        """
        Initialize the entry object
        :param data: string in the following format
        word : meaning
        """
        [[word, definition]] = self.pattern.findall(data)
        self._word = word.strip()
        self._definition = definition.strip()

    def is_valid(self):
        return self._word != "" and self._definition != ""

    def get_data(self) -> Dict:
        """Function to convert it into data format for db insertion"""
        return {
            'word': self._word,
            'definition': self._definition
        }

    def str(self) -> str:
        """return str"""
        return f"{self._word}: {self._definition}"

