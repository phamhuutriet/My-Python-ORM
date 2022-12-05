from EntSchema.EntSchemaInterface import EntSchemaInterface
from CodeGenerator.CodegenHelper import CodegenHelper
from enums.EntFieldEnums import EntFieldEnums
from EntMutator.SQLHelper import SQLHelper
from CodeGenerator.EntClassCodegenHelper import EntClassCodegenHelper
import os


class EntClassCodegen:
    def __init__(self, schema: EntSchemaInterface) -> None:
        self.schema = schema
        self.helper = EntClassCodegenHelper(schema=schema)
        # destined file paths
        self.MUTATOR_PATH = "./CodeGenerator/templates/EntMutatorTemplate.txt"
        self.SCHEMA_PATH = "./CodeGenerator/templates/EntQuerierTemplate.txt"
        self.ENT_PATH = "./CodeGenerator/templates/EntTemplate.txt"
        # String const
        self.ENT = self.schema.tableName().value
        self.SCHEMA = f"{self.ENT}Schema"

    def run(self) -> None:
        self.createDirectory()
        self.createEnt()
        self.createEntMutator()
        self.createEntQuerier()
        SQLHelper.createTable(
            table_name=self.ENT,
            table_description=self.helper.getTableDescriptionString(),
        )

    def createDirectory(self) -> None:
        try:
            os.mkdir(f"./demo/{self.ENT}")
        except:
            print("Directory already existed. Move to generating other classes")

    def createEnt(self) -> None:
        parameters_dict = {
            "__SCHEMA_PATH__": f"demo.{self.ENT}.{self.SCHEMA}",
            "__ENT_SCHEMA__": self.SCHEMA,
            "__INIT_WITH_DEFAULT__": self.helper.getInitStringWithDefault(),
            "__SET_FIELDS__": self.helper.getSetFieldsString(),
            "__FIELDS_GETTERS_SETTERS_METHODS__": self.helper.getFieldsGetterAndSetterMethods(),
            "__ENT__": self.ENT,
        }
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.ENT}/{self.ENT}.py",
            file_context=CodegenHelper.replace(self.ENT_PATH, parameters_dict),
        )

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
            "__INIT__": self.helper.getInitString(),
        }
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.ENT}/{querier_name}.py",
            file_context=CodegenHelper.replace(self.SCHEMA_PATH, parameters_dict),
        )
