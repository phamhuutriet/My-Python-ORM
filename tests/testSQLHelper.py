import unittest
from EntMutator.SQLHelper import SQLHelper
from unittest_data_provider import data_provider


class TestSQLHelper(unittest.TestCase):
    def createUpdateStringDataProvider():
        update_dict_list = [
            {"name": "Triet", "age": 18},
            {"name": "Mai", "balance": "1000"},
        ]
        result_str_list = ["name = Triet,age = 18", "name = Mai,balance = 1000"]
        return (
            (update_dict, result_str)
            for update_dict, result_str in zip(update_dict_list, result_str_list)
        )

    @data_provider(createUpdateStringDataProvider)
    def testCreateUpdateString(self, update_dict: dict, result_str: str):
        self.assertEqual(SQLHelper.createUpdateString(update_dict), result_str)
