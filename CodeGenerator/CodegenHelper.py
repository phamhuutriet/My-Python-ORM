class CodegenHelper:
    @staticmethod
    def replace(template_path: str, parameter_dict: dict) -> str:
        """This method replace the template's parameter with real value from respective key in parameter dict"""
        ans = CodegenHelper.openFile(template_path)
        for parameter_name, parameter_value in parameter_dict.items():
            ans = ans.replace(parameter_name, parameter_value)
        return ans

    @staticmethod
    def writeFile(destined_path: str, file_context: str) -> None:
        """This method create a new file with file context and locate in the destined path"""
        new_file = open(destined_path, "w")
        new_file.write(file_context)
        new_file.close()
        return

    @staticmethod
    def openFile(file_path: str) -> str:
        file = open(file_path, "r")
        ans = file.read()
        file.close()
        return ans
