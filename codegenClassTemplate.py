from demo.User.UserSchema import UserSchema
from CodeGenerator.EntClassCodegen import EntClassCodegen


def main():
    codegen_class = EntClassCodegen(schema=UserSchema())
    codegen_class.run()


if __name__ == "__main__":
    main()
