try:
    import io as StringIO
except ImportError:
    import StringIO
import json

class DyDB(object):
    """A Dynamic DataBase Object"""

    def __init__(self):
        """Init setup"""
        self.data_file = StringIO.StringIO()
        data_temp = unicode(dict())
        self.data_file.write(json.dumps(data_temp, ensure_ascii=False))

    def set(self, key, value):
        """Set a Key, Value pair"""

    def val(self, key):
        """Get a Value from a Key"""

    def key(self, value):
        """Get a List of Keys from a Value"""

    def store(self, data):
        """Store the database to a file-like object"""

    def fetch(self):
        """Fetch the database from a file-like object"""

testDB = DyDB()
print(dir(testDB))
