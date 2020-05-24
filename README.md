## Dictionary Database (dictdb)

A simple console based application for users to build their own dictionary with their own definition.
I have been keeping a list of new words or vocabularies that I am unfamiliar with, and I thought it would be useful to have an application doing that for me. 

This program will create a `data/database.json` file which is a TinyDB flat database (json) file. 
This file will store all the entries you have added in to the dictionary


## Features
- add, remove, delete, list, export, import dictionary

## Data Format
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

## Usage
```
usage:
       ___      __      ____
  ____/ (_)____/ /_____/ / /_
 / __  / / ___/ __/ __  / __ \
/ /_/ / / /__/ /_/ /_/ / /_/ /
\__,_/_/\___/\__/\__,_/_.___/

dev: the-c0d3r

       [-h] [-i] [-s SEARCH] [-a ADD] [-d DELETE] [-e EDIT] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     interactive mode for all entries
  -s SEARCH, --search SEARCH
                        search word
  -a ADD, --add ADD     add new word
  -d DELETE, --delete DELETE
                        delete word
  -e EDIT, --edit EDIT  edit the existing definitions
  -l, --list            list all words
```

`dictdb` without any arguments will print usage. But if the stdout is piped to other programs, it will list everything.

`dictdb -s word` will do a search for the word. This will print the word if matched, it also support partial match.

`dictdb -a word` this means add new word, but the "word" here needs to follow the standard data format declared above. e.g. `dictdb -a "test:definition"
   
`dictdb -d word` will delete the word if it exists.

`dictdb -e word` will launch editor with the word and definition if it exists, else empty editor will allow you to add new.

`dictdb -i` will launch editor with all the words and definitions. Any changes made in the editor will overwrite the database

When triggering `-i` or `-e`, it will use `$EDITOR` env variable and launch the editor. 
For more info, refer to [python-editor](https://pypi.org/project/python-editor/)

## Import & Export

```bash
dictdb < dict.txt
```
Import `dict.txt` to the database.

```bash
dictdb > export.txt
```
Export the database content into `export.txt`

## TODO
- [x] Record user's own definition entry
- [x] View and edit user's entry
- [x] Edit entry in vim
- [x] Import words from file, e.g. `dictdb < dict.txt`
- [x] Export functionality, e.g. `dictdb > export.txt`
- [x] Interactive mode of editing
- [ ] Asciinema screen record for README
- [ ] Custom db location (or just do a symlink?)
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
