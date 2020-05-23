## Dictionary Database (dictdb)

Purpose : a tool for me to record new english words that I learned

This program will create a `data/database.json` file which is a TinyDB flat database (json) file. 
This file will store all the entries you have added in to the dictionary

## Features
- Able to search the popular dictionaries for definition, as well as write your own definition 
- Able to export your custom dictionary into a txt file
- Randomly show word of the day from words you have entered into the database

## Usage

```bash
usage: Dictionary Database [-h] [-i INTERACTIVE] [-s SEARCH] [-a ADD]
                           [-d DELETE] [-m MODIFY] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -i INTERACTIVE, --interactive INTERACTIVE
                        interactive mode
  -s SEARCH, --search SEARCH
                        search word
  -a ADD, --add ADD     add new word
  -d DELETE, --delete DELETE
                        delete word
  -m MODIFY, --modify MODIFY
                        modify the existing definitions
  -l, --list            list all words (tip: use 'more')
```

## TODO
- [x] Record user's own definition entry
- [x] View and edit user's entry
- [x] Edit entry in vim
- [ ] Asciinema screen record for README
- [ ] Interactive mode of editing
- [ ] Custom db location
- [ ] Add free dictionary for offline lookup
- [ ] Search through offline dict
- [ ] Export functionality (txt for now)
- [ ] Import words from file (txt for now)
- [ ] deployment setup
    - [ ] travis pytest
    - [ ] console script
    - [ ] pypi
