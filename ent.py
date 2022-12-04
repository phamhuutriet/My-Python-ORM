from CodeGenerator.EntClassCodegen import EntClassCodegen
import sys
import os


def find(schema_name, path):
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
        print(find(schema_name, "./"))


if __name__ == "__main__":
    main()
