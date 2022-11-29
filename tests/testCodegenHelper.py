import unittest
from unittest_data_provider import data_provider
from unittest.mock import patch
from CodeGenerator.CodegenHelper import CodegenHelper


class testCodegenHelper(unittest.TestCase):
    def replaceDataProvider(self):
        file_context_list = [
            """class __CLASS_NAME__:
                                  def get__ATTRIBUTE__():
                                      pass
                                  
                                  def set__ATTRIBUTE__():
                                      pass
                          """
        ]
        parameters_dict_list = [
            {"__CLASS_NAME__": "EntSchema", "__ATTRIBUTE__": "Name"}
        ]
        ans_list = [
            """class EntSchema:
                                  def getName():
                                      pass
                                  
                                  def setName():
                                      pass
                          """
        ]
        return (
            (file_context, parameters_dict, ans)
            for file_context, parameters_dict, ans in zip(
                file_context_list, parameters_dict_list, ans_list
            )
        )

    @patch("CodeGenerator.CodegenHelper.CodegenHelper.openFile")
    def testReplace(self, mocked_open_file):
        for file_context, parameters_dict, ans in self.replaceDataProvider():
            mocked_open_file.return_value = file_context
            self.assertEqual(CodegenHelper.replace("", parameters_dict), ans)
