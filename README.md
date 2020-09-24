## Dictionary Database (dictdb)

A simple console based application for users to build their own dictionary with their own definition.

I have been keeping my own dictionary, a list of words and their definitions, for the new obscure words that I found. But since the list has grown to over 300 words, I found it hard to manually sort through, search, and add new entries.

Therefore, I created this program to help me make all this easier. I tried to follow the unix principle, do one thing and do it good, as well as the ability to natively support the piping, redirection to and fro stdin/stdout to make it easier to use. 

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Data Format](#data-format)
- [Import and Export](#import-and-export)
- [Todo](#todo)
- [Feature Wishlist](#feature-wishlist)


## Features
- add, remove, delete, list, export, import dictionary

## Usage

[![asciicast](https://asciinema.org/a/sD6t5jd2pm4TU9XNIe1pF2ENZ.svg)](https://asciinema.org/a/sD6t5jd2pm4TU9XNIe1pF2ENZ)

- `dictdb` without any arguments will print usage. But if the stdout is piped to other programs, it will list everything.

- `dictdb -s word` will do a search for the word. This will print the word if matched, it also support partial match.

- `dictdb -a word` this means add new word, but the "word" here needs to follow the standard data format declared above. e.g. `dictdb -a "test:definition"
   
- `dictdb -d word` will delete the word if it exists.

- `dictdb -e word` will launch editor with the word and definition if it exists, else empty editor will allow you to add new.

- `dictdb -i` will launch editor with all the words and definitions. Any changes made in the editor will overwrite the database

When triggering `-i` or `-e`, it will use `$EDITOR` env variable and launch the editor. 
For more info, refer to [python-editor](https://pypi.org/project/python-editor/)


## Installation
Installation steps will currently be manual. It will be automated with `setup.py` later into a console script. 
```bash
git clone https://github.com/the-c0d3r/dictdb.git
cd dictdb
pip3 install -r requirements.txt

ln -s ${PWD}/dictdb /usr/local/bin/dictdb
chmod +x ./dictdb
```

## Data Format
This program will create a `data/database.json` file which is a TinyDB flat database (json) file. 
This file will store all the entries you have added in to the dictionary.

The following data format applies to import, export, edit, add. 
It is a simple schema where by the word/phrase before the first ':' is considered the word. Then whatever is after the first ':' is considered the definition. Definition can also contain ':' or any other characters.

All of the following format is supported
```
word1: definition1
word2 : definition2
word3:definition3
word3 :definition3
word4:word4:test
```

## Import and Export

```bash
dictdb < dict.txt
```
Import `dict.txt` to the database.

**WARNING: Importing will overwrite all existing data**

```bash
dictdb > export.txt
```
Export the database content into `export.txt`

## Todo
- [x] Record user's own definition entry
- [x] View and edit user's entry
- [x] Edit entry in vim
- [x] Import words from file, e.g. `dictdb < dict.txt`
- [x] Export functionality, e.g. `dictdb > export.txt`
- [x] Interactive mode of editing
- [x] Asciinema screen record for README
- [x] Custom db location (or just do a symlink?)
- [ ] Official dictionary
    - [ ] Add free dictionary for offline lookup
    - [ ] Search through offline dict
- [ ] deployment setup
    - [ ] travis pytest
    - [ ] console script
    - [ ] pypi

## Feature Wishlist
- create flashcards
- keep track of the stats, top 10 popular words from search
- email the summary of new words
- Able to search the popular dictionaries for definition
- Randomly show word of the day from words you have entered into the database

> "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away." ~ Antoine de Saint-Exupery

PR is welcomed, as well as criticism and comments.
