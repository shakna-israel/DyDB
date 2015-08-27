# DyDB - Dynamic DataBase

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

# Grab a key's value:
someData.value("myKey")

# Grab a list of keys that have a certain value:
someData.key(False)

# Store the Database to a temporary file:
someData.store()

# Load the Database from a temporary file:
someData.fetch()

# Store the Database to a particular file:
someData.store("myfile.json")

# Load the Database from a particular file:
someData.fetch("myfile.json")
```

**Note:**

* There is only one temporary file. Its easy to overwrite.
* The database is ***not*** performant.
* The top-level key *_id* is reserved. You can overwrite it, but in future, this may cause unexpected behaviour.

## Install

Currently, there is no install process.

DyDB.py is a standalone file that can be dropped into the folder of any project where you want to import it.

This will change in the future - it will remain a standalone file you can drop-in, but will be released to PyPI, (making it pip installable), but is not yet ready.

## Contributing

Currently, the project is at a very early stage. (Less than an hour at time of writing).

This means that there is not yet an apparent style guide for contributing new features, and bugs have not been identified.

However, some plans that exist may be contributable:

* Temporary file storage and recall based on *_id* key, and maybe process ID, to allow for multiple temporary files to coexist.
* Automatic temporary file storage. (Depending on the above.)
* Tests. Tests. More tests. Make coverage scream 100%. (I prefer *nose*).
* Multiple database modifications at once. Probably allow *DyDB.set* to take: a single key value, a key-value pair, a dictionary of key-value pairs.
* Multiple database key fetching. Probably allow *DyDB.value* to take: a single key value, a list of key values.
