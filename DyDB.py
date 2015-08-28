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
import os
import json

class DyDB(object):
    """A Dynamic DataBase Object"""

    def __init__(self):
        """Init setup"""
        self.DataFileObject = StringIO.StringIO()
        data_temp = {"_id":str(uuid.uuid4())}
        self.DataFileObject.write(json.dumps(data_temp, ensure_ascii=False))

    def set(self, key, value=False):
        """Set a Key, Value pair"""
        if type(key) == list:
            temp_dict = {}
            for item in key:
                temp_dict[item] = False
        elif type(key) == dict:
            temp_dict = key.copy()
        else:
            temp_dict = {key: value}
        existing_data = json.loads(self.DataFileObject.getvalue())
        new_data = existing_data.copy()
        new_data.update(temp_dict)
        self.DataFileObject.truncate(0)
        self.DataFileObject.seek(0)
        self.DataFileObject.write(json.dumps(new_data, ensure_ascii=False))
        return True

    def value(self, key):
        """Get a Value from a Key"""
        existing_data = json.loads(self.DataFileObject.getvalue())
        if type(key) == list:
            ret_dict = {}
            for item in existing_data:
                for compare in key:
                    if item == compare:
                        ret_dict[item] = existing_data[item]
            return ret_dict
        else:
            return existing_data[key]

    def key(self, value):
        """Get a List of Keys from a Value"""
        existing_data = json.loads(self.DataFileObject.getvalue())
        ret_list = []
        for key, val in existing_data.items():
            if val == value:
                ret_list.append(key)
        return ret_list

    def store(self, dataFile=False):
        """Store the database to disk"""
        existing_data = json.loads(self.DataFileObject.getvalue())
        if dataFile:
            with open(dataFile, 'w+') as openFile:
                openFile.write(json.dumps(existing_data, sort_keys=True, indent=4, separators=(',', ': ')))
            return True
        else:
            if not os.path.isdir(os.path.expanduser("~/.DyDB")):
                os.makedirs(os.path.expanduser("~/.DyDB"))
            with open(os.path.expanduser("~/.DyDB/temp.dydb"), "w+") as openFile:
                openFile.write(json.dumps(existing_data, sort_keys=True, indent=4, separators=(',', ': ')))
            return True

    def fetch(self, dataFile=False):
        """Fetch the database from disk"""
        self.DataFileObject.truncate(0)
        self.DataFileObject.seek(0)
        if dataFile:
            with open(dataFile, 'r') as openFile:
                json_data = json.load(openFile)
        else:
            with open(os.path.expanduser("~/.DyDB/temp.dydb"), "r") as openFile:
                json_data = json.load(openFile)
        self.DataFileObject.write(json.dumps(json_data, ensure_ascii=False))
        return True
