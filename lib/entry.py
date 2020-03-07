#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict


class Entry:
    """Dictionary Entry object"""

    def __init__(self, word: str, meaning: str):
        """
        Initialize the entry object
        :param word: the word to store
        :param meaning: Meaning of the word
        """
        self._word = word
        self._meaning = meaning

    def get_data(self) -> Dict:
        """Function to convert it into data format for db insertion"""
        return {
            'word': self._word,
            'definition': self._meaning
        }

    def str(self) -> str:
        """return str"""
        return f"{self._word}: {self._meaning}"

