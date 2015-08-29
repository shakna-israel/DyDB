import coverage
import DyDB
import test
import unittest

class TestCoverage(unittest.TestCase):

    def test_coverage(self):
        """Test that code coverage is above 60%"""
        # 60% only, as it averages coverage between tests and DyDB

        cov = coverage.coverage()
        tester = test.TestDyDB()
        cov.start()

        tester.test_object_init()
        tester.test_object_init_id()
        tester.test_object_init_id_uuid()
        tester.test_dydb_set_single_value()
        tester.test_dydb_set_single_value_is_false()
        tester.test_dydb_set_key_pair()
        tester.test_dydb_set_key_pair_value()
        tester.test_dydb_set_key_list()
        tester.test_dydb_set_key_list_value()
        tester.test_dydb_set_key_dict()
        tester.test_dydb_set_key_dict_value()
        tester.test_dydb_value()
        tester.test_dydb_value_correct()
        tester.test_dydb_value_dict()
        tester.test_dydb_value_dict_value()
        tester.test_dydb_key()
        tester.test_dydb_key_list()
        tester.test_dydb_key_correct()
        tester.test_dydb_key_all()
        tester.test_store_temp_structure()
        tester.test_store_temp_data()
        tester.test_store_specific_structure()
        tester.test_store_specific_data()
        tester.test_fetch_temp()
        tester.test_fetch_temp_data()
        tester.test_dydb_pop()
        tester.test_dydb_pop_value()
        tester.test_dydb_pop_list()

        cov.stop()

        final_coverage = int(cov.report())
        if final_coverage < 60:
            assert False
        else:
            pass
