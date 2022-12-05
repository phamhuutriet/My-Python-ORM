from CodeGenerator.CodegenHelper import CodegenHelper
import sys
import os


def find(schema_name, path):
    """Find the file with schema name and return its module path"""
    schema_file_name = schema_name + ".py"
    for root, dirs, files in os.walk(path):
        if schema_file_name in files:
            return f"{processRoot(root)}.{schema_name}"


def processRoot(root: str) -> str:
    dirs = root.split("/")
    return ".".join(dirs[1:])


def main():
    try:
        schema_name = sys.argv[1]
    except:
        print("Invalid input")
        exit(2)
    else:
        parameters_dict = {
            "__SCHEMA_PATH__": find(schema_name, "./"),
            "__SCHEMA__": schema_name,
        }
        CodegenHelper.writeFile(
            destined_path="./codegenClass.py",
            file_context=CodegenHelper.replace(
                template_path="./CodeGenerator/templates/CodegenClassTemplate.txt",
                parameter_dict=parameters_dict,
            ),
        )
        os.system("python3 codegenClass.py")
        os.remove("./codegenClass.py")


if __name__ == "__main__":
    main()
