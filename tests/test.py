import unittest
import DyDB
import json
import os

class TestDyDB(unittest.TestCase):

    def test_object_init(self):
        """Test that we can create a DyDB object"""
        testObject = DyDB.DyDB()
        if testObject.DataFileObject:
            pass
        else:
            assert False

    def test_object_init_id(self):
        """Test that an initial DyDB object has an _id"""
        testObject = DyDB.DyDB()
        testData = json.loads(testObject.DataFileObject.getvalue())
        if testData["_id"]:
            pass
        else:
            assert False

    def test_object_init_id_uuid(self):
        """Test that an initial DyDB object has an _id, and that its value is a UUID"""
        testObject = DyDB.DyDB()
        testData = json.loads(testObject.DataFileObject.getvalue())
        if testData["_id"]:
            if len(testData["_id"]) == 36:
                pass
            else:
                assert False
        else:
            assert False

    def test_dydb_set_single_value(self):
        """Test that we can set a key, without setting its value"""
        testObject = DyDB.DyDB()
        testObject.set("testKey")
        testData = json.loads(testObject.DataFileObject.getvalue())
        if "testKey" in testData:
            pass
        else:
            print(testData)
            assert False

    def test_dydb_set_single_value_is_false(self):
        """Test that we can set a key, without setting its value, and that its value will be False"""
        testObject = DyDB.DyDB()
        testObject.set("testKey")
        testData = json.loads(testObject.DataFileObject.getvalue())
        if testData["testKey"] == False:
            pass
        else:
            assert False

    def test_dydb_set_key_pair(self):
        """Test that we can set a key value pair"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        testData = json.loads(testObject.DataFileObject.getvalue())
        if "testKey" in testData:
            pass
        else:
            assert False

    def test_dydb_set_key_pair_value(self):
        """Test that we can set a key value pair, and that its value is correct"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        testData = json.loads(testObject.DataFileObject.getvalue())
        if testData["testKey"] == "testValue":
            pass
        else:
            assert False
    
    def test_dydb_set_key_list(self):
        """Test that we can set a list of keys"""
        testObject = DyDB.DyDB()
        testObject.set(["mykey","testkey"])
        testData = json.loads(testObject.DataFileObject.getvalue())
        if "myKey" in testData:
            if "testKey" in testData:
                pass
            else:
                assert False
        else:
            assert False

    def test_dydb_set_key_list_value(self):
        """Test that we can set a list of keys"""
        testObject = DyDB.DyDB()
        testObject.set(["myKey", "testKey"])
        testData = json.loads(testObject.DataFileObject.getvalue())
        if testData["myKey"] == False:
            if testData["testKey"] == False:
                pass
            else:
                assert False
        else:
            assert False

    def test_dydb_value(self):
        """Test that we can get a value from a key"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        if testObject.value("testKey"):
            pass
        else:
            assert False

    def test_dydb_value_correct(self):
        """Test that we can get the correct value from a key"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        if testObject.value("testKey") == "testValue":
            pass
        else:
            assert False

    def test_dydb_key(self):
        """Test that we can get a list of keys from a value"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        if testObject.key("testValue"):
            pass
        else:
            assert False

    def test_dydb_key_list(self):
        """Test that we get a list back when asking for a list of keys from a value"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        if type(testObject.key("testValue")) == list:
            pass
        else:
            assert False

    def test_dydb_key_correct(self):
        """Test that the list we get back, when asking for a list of keys, gives us the correct value"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        if "testKey" in testObject.key("testValue"):
            pass
        else:
            assert False

    def test_store_temp_structure(self):
        """Test that when storing a temp file, it can generate the folder structure"""
        testObject = DyDB.DyDB()
        testObject.store()
        if os.path.isdir(os.path.expanduser("~/.DyDB")):
            pass
        else:
            assert False

    def test_store_temp_data(self):
        """Test that when storing a temp file, it stores the data correctly"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        testObject.store()
        with open(os.path.expanduser("~/.DyDB/temp.dydb"), "r") as openFile:
            json_data = json.load(openFile)
        if "testKey" in json_data:
            pass
        else:
            assert False

    def test_store_specific_structure(self):
        """Test that when storing a specific file, it gets created"""
        testObject = DyDB.DyDB()
        testObject.store("tempFile.json")
        if os.path.isfile("tempFile.json"):
            pass
        else:
            assert False

    def test_store_specific_data(self):
        """Test that when storing a specific file, it stores the data correctly"""
        testObject = DyDB.DyDB()
        testObject.set("testKey", "testValue")
        testObject.store("tempFile.json")
        with open("tempFile.json", "r") as openFile:
            json_data = json.load(openFile)
        if "testKey" in json_data:
            pass
        else:
            assert False

    def test_fetch_temp(self):
        """Test that we can fetch a temporary file"""
        testObject = DyDB.DyDB()
        testDataDict = {"testKey":"testValue"}
        if not os.path.isdir(os.path.expanduser("~/.DyDB")):
            os.makedirs(os.path.expanduser("~/.DyDB"))
        with open(os.path.expanduser("~/.DyDB/temp.dydb"), "w+") as openFile:
            openFile.write(json.dumps(testDataDict, sort_keys=True, indent=4, separators=(',', ': ')))
        testObject.fetch()
        testData = json.loads(testObject.DataFileObject.getvalue())
        if "testKey" in testData:
            pass
        else:
            assert False

    def test_fetch_temp_data(self):
        """Test that we can fetch the correctly value from a temporary file"""
        testObject = DyDB.DyDB()
        testDataDict = {"testKey":"testValue"}
        if not os.path.isdir(os.path.expanduser("~/.DyDB")):
            os.makedirs(os.path.expanduser("~/.DyDB"))
        with open(os.path.expanduser("~/.DyDB/temp.dydb"), "w+") as openFile:
            openFile.write(json.dumps(testDataDict, sort_keys=True, indent=4, separators=(',', ': ')))
        testObject.fetch()
        testData = json.loads(testObject.DataFileObject.getvalue())
        if testData["testKey"] == "testValue":   
            pass
        else:
            assert False
