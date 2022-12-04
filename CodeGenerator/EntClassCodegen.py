from EntSchema.EntSchemaInterface import EntSchemaInterface
from CodeGenerator.CodegenHelper import CodegenHelper


class EntClassCodegen:
    def __init__(self, schema: EntSchemaInterface) -> None:
        self.schema = schema

    def run(self) -> None:
        # Generate Ent

        # Generate EntMutator
        self.createEntMutator()

        # Generate EntQuerier

        # Generate SQL tables
        pass

    def createEntMutator(self) -> None:
        template_path = "./CodeGenerator/templates/EntMutatorTemplate.txt"
        parameters_dict = {"__MUTATOR__": self.schema.tableName().value}
        CodegenHelper.writeFile(
            destined_path=f"./demo/{self.schema.tableName().value}",
            file_context=CodegenHelper.replace(template_path, parameters_dict),
        )
