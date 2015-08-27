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
        data_temp = {}
        self.data_file.write(json.dumps(data_temp), sort_keys=True, indent=4, separators=(',', ': '))
        print(self.data_file.getvalue())
        self.data_home = json.load(self.data_file)

    def set(self, key, value):
        """Set a Key, Value pair"""

    def get_val(self, key):
        """Get a Value from a Key"""

    def get_key(self, value):
        """Get a List of Keys from a Value"""

    def data_store(self, data):
        """Store the database to a file-like object"""
        dataStore = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        return self.data_file.write(dataStore)

    def data_fetch(self):
        """Fetch the database from a file-like object"""
        return json.load(self.data_file)

testDB = DyDB()
testData = {"test":"val"}
DyDB.data_store(testData)
print(DyDB.data_fetch())
