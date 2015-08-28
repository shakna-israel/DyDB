# DyDB - Dynamic DataBase

[![Build Status](https://travis-ci.org/shakna-israel/DyDB.svg?branch=master)](https://travis-ci.org/shakna-israel/DyDB) [![Code Health](https://landscape.io/github/shakna-israel/DyDB/master/landscape.svg?style=flat)](https://landscape.io/github/shakna-israel/DyDB/master)

## For the love of all that is holy, Why?

### TL;DR

I wanted a document-db, but couldn't find what I wanted.

---

Though there are many databases out there, that are powerful, and incredibly more performant than DyDB, I have found several circumstances in my work recently, when I needed a nice, simple document-oriented database that can talk to Python, but haven't been allowed to install any dependencies.

I was left with JSON, PickleDB, and SQLite.

I don't particularly like the SQL language, it feels outdated and clunky.

PickleDB (which now uses json) is a nice project, but seems to be irregularly maintained, and can't serialise lists.

Thus: DyDB.

I don't expect that anyone will like or use it.

**It's probably not production-safe.**

## Usage

Using DyDB is fairly simple, but may feel fairly unconventional.

```python
# Import the DB Engine:
from DyDB import DyDB

# Create a DB object:
someData = DyDB()

# Set an empty Key:
someData.set("myKey")

# Set several empty Keys:
someData.set(["some key","testKey","SweetKey"])

# Set a Key with Value:
someData.set("otherKey", "myValue")

# Set several Keys with Values:
someData.set({"key":"value","somekey":"somevalue"})

# Grab a key's value:
someData.value("myKey")

# Grab a dictionary of key values, from a list of keys:
someData.value(["myKey, "otherKey"])

# Grab a list of keys that have a certain value:
someData.key("myValue")

# Grab all available keys:
someData.key()

# Remove a particular key from the Database:
someData.pop("someKey")

# Remove a list of keys from the Database:
someData.pop(["someKey","someOtherKey"])

# Store the Database to a temporary file:
someData.store()

# Load the Database from a temporary file:
someData.fetch()

# Store the Database to a particular file:
someData.store("myfile.json")

# Load the Database from a particular file:
someData.fetch("myfile.json")
```

## Important Notes:

* Though DyDB attempts to store a temporary file for each Database generated, there is an infintisimally small chance of collision, and one temporary file will overwrite another.
    * TL;DR - Explicitly naming a file when storing is better.
    * All temporary files are stored in ```~/.DyDB``` or ```C:\Users\<your user>\.DyDB```
* The database is ***not*** performant.
* The top-level key *_id* is reserved. Overwriting it may cause the automatic temporary file storage to... Fail.
* PyPy is not currently supported.

## Install

Currently, there is no install process.

DyDB.py is a standalone file that can be dropped into the folder of any project where you want to import it.

This will change in the future - it will remain a standalone file you can drop-in, but will be released to PyPI, (making it pip installable), but is not yet ready.

## Contributing

Currently, the project is at a very early stage. (Think "pre-alpha").

This means that there is not yet an apparent style guide for contributing new features, and bugs have not been identified.

However, some plans that exist may be contributable, they can be found [here](https://github.com/shakna-israel/DyDB/labels/enhancement).
