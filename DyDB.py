# Force Python 2 to treat print as a proper function, not a statement
from __future__ import print_function

# Import Unicode for Python 2 to make it work... Nicely.
from __future__ import unicode_literals

# Grabbing the right library between Python 2 and 3
try:
    import io as StringIO
except ImportError:
    import StringIO

import uuid
import json

class DyDB(object):
    """A Dynamic DataBase Object"""

    def __init__(self):
        """Init setup"""
        self.DataFileObject = StringIO.StringIO()
        data_temp = {"_id":str(uuid.uuid4())}
        self.DataFileObject.write(json.dumps(data_temp, ensure_ascii=False))

    def set(self, key, value):
        """Set a Key, Value pair"""
        temp_dict = {key: value}
        existing_data = json.loads(self.DataFileObject.getvalue())
        new_data = existing_data.copy()
        new_data.update(temp_dict)
        self.DataFileObject.truncate(0)
        self.DataFileObject.seek(0)
        self.DataFileObject.write(json.dumps(new_data, ensure_ascii=False))

    def value(self, key):
        """Get a Value from a Key"""

    def key(self, value):
        """Get a List of Keys from a Value"""

    def store(self, data):
        """Store the database to disk"""

    def fetch(self):
        """Fetch the database from disk"""

testDB = DyDB()
[print(x) for x in dir(testDB)]
