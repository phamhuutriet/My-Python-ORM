from EntSchema.EntSchemaInterface import EntSchemaInterface
from CodeGenerator.CodegenHelper import CodegenHelper
import os


class EntClassCodegen:
    def __init__(self, schema: EntSchemaInterface) -> None:
        self.schema = schema

        # destined file paths
        self.MUTATOR_PATH = "./CodeGenerator/templates/EntMutatorTemplate.txt"
        self.SCHEMA_PATH = "./CodeGenerator/templates/EntQuerierTemplate.txt"

        # String const
        self.ENT = self.schema.tableName().value
        self.SCHEMA = f"{self.ENT}Schema"

    def run(self) -> None:
        self.createDirectory()
        # Generate Ent

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
