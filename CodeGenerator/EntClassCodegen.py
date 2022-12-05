from EntSchema.EntSchemaInterface import EntSchemaInterface
from CodeGenerator.CodegenHelper import CodegenHelper
import os


class EntClassCodegen:
    def __init__(self, schema: EntSchemaInterface) -> None:
        self.schema = schema

    def run(self) -> None:
        self.createDirectory()
        # Generate Ent

        # Generate EntMutator
        self.createEntMutator()

        # Generate EntQuerier

        # Generate SQL tables
        pass

    def createDirectory(self) -> None:
        os.mkdir(f"./demo/{self.schema.tableName().value}")

    def createEntMutator(self) -> None:
        template_path = "./CodeGenerator/templates/EntMutatorTemplate.txt"
        mutator_name = f"{self.schema.tableName().value}Mutator"
        parameters_dict = {"__MUTATOR__": mutator_name}
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.schema.tableName().value}/{mutator_name}.py",
            file_context=CodegenHelper.replace(template_path, parameters_dict),
        )
