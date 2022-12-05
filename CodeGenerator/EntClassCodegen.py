from EntSchema.EntSchemaInterface import EntSchemaInterface
from CodeGenerator.CodegenHelper import CodegenHelper
from enums.EntFieldEnums import EntFieldEnums
import os


class EntClassCodegen:
    def __init__(self, schema: EntSchemaInterface) -> None:
        self.schema = schema

        # destined file paths
        self.MUTATOR_PATH = "./CodeGenerator/templates/EntMutatorTemplate.txt"
        self.SCHEMA_PATH = "./CodeGenerator/templates/EntQuerierTemplate.txt"
        self.ENT_PATH = "./CodeGenerator/templates/EntTemplate.txt"

        # String const
        self.ENT = self.schema.tableName().value
        self.SCHEMA = f"{self.ENT}Schema"

        self.DEFAULT_VALUE_DICT = {
            EntFieldEnums.INT: 0,
            EntFieldEnums.STRING: '""',
            EntFieldEnums.FLOAT: 0.0,
        }

    def run(self) -> None:
        self.createDirectory()
        # Generate Ent
        self.createEnt()

        # Generate EntMutator
        self.createEntMutator()

        # Generate EntQuerier
        self.createEntQuerier()

        # Generate SQL tables
        pass

    def createDirectory(self) -> None:
        try:
            os.mkdir(f"./demo/{self.ENT}")
        except:
            print("Directory already existed. Move to generating other classes")

    def createEntMutator(self) -> None:
        mutator_name = f"{self.ENT}Mutator"
        parameters_dict = {"__MUTATOR__": mutator_name}
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.ENT}/{mutator_name}.py",
            file_context=CodegenHelper.replace(self.MUTATOR_PATH, parameters_dict),
        )

    def createEntQuerier(self) -> None:
        querier_name = f"{self.ENT}Querier"
        parameters_dict = {
            "__ENT__": self.ENT,
            "__ENT_PATH__": f"demo.{self.ENT}.{self.ENT}",
            "__SCHEMA_PATH__": f"demo.{self.ENT}.{self.SCHEMA}",
            "__ENT_SCHEMA__": self.SCHEMA,
            "__INIT__": self.getInitString(),
        }
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.ENT}/{querier_name}.py",
            file_context=CodegenHelper.replace(self.SCHEMA_PATH, parameters_dict),
        )

    def getInitString(self) -> str:
        set_fields_strings = []
        for field_name in self.schema.getFieldsNames():
            set_fields_strings.append(f'{field_name}=result["{field_name}"]')
        return ", ".join(set_fields_strings)

    def getInitStringWithDefault(self) -> str:
        set_fields_strings = []
        for field in self.schema.getFields():
            set_field_string = f"{field.getName()}: {field.getType().value} = {self.DEFAULT_VALUE_DICT[field.getType()]}"
            set_fields_strings.append(set_field_string)
        return ", ".join(set_fields_strings)

    def getSetFieldsString(self) -> str:
        set_fields_strings = []
        for i, field_name in enumerate(self.schema.getFieldsNames()):
            set_field_string = f"self.{field_name} = {field_name}"
            if i != 0:
                set_field_string = "        " + set_field_string
            set_fields_strings.append(set_field_string)
        return "\n".join(set_fields_strings)

    def getFieldsGetterAndSetterMethods(self) -> str:
        set_fields_strings = []
        for i, field in enumerate(self.schema.getFields()):
            is_first = i == 0
            set_fields_strings.append(
                self.getFieldGetterAndSetterMethod(
                    field.getName(), field.getType(), is_first
                )
            )
        return "\n".join(set_fields_strings)

    def getFieldGetterAndSetterMethod(
        self, field_name: str, field_type: EntFieldEnums, is_first: bool
    ) -> str:
        uppercase_field_name = field_name[0].upper() + field_name[1:].lower()
        first_tab = "    "
        if is_first:
            first_tab = ""
        getter_s = f"""{first_tab}def get{uppercase_field_name}(self) -> {field_type.value}:
        return self.{field_name}
        """
        setter_s = f"""    def set{uppercase_field_name}(self, {field_name}: {field_type.value}) -> None:
        self.{field_name} = {field_name}
        """
        return getter_s + "\n" + setter_s

    def createEnt(self) -> None:
        parameters_dict = {
            "__SCHEMA_PATH__": f"demo.{self.ENT}.{self.SCHEMA}",
            "__ENT_SCHEMA__": self.SCHEMA,
            "__INIT_WITH_DEFAULT__": self.getInitStringWithDefault(),
            "__SET_FIELDS__": self.getSetFieldsString(),
            "__FIELDS_GETTERS_SETTERS_METHODS__": self.getFieldsGetterAndSetterMethods(),
        }
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.ENT}/{self.ENT}.py",
            file_context=CodegenHelper.replace(self.ENT_PATH, parameters_dict),
        )
