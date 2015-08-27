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
