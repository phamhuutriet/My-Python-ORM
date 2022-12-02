from EntSchema.EntSchemaInterface import EntSchemaInterface
from EntSchema.EntField import EntField
from EntSchema.EntEdge import EntEdge
from enums.DatabaseEnums import DatabaseEnums
from typing import List


class UserSchema(EntSchemaInterface):
    def __init__(self) -> None:
        pass

    def getTableName(self, show_fields: bool = False) -> str:
        if not show_fields:
            return DatabaseEnums.USER_TABLE.value
        fields_string = ",".join([field.getName() for field in self.getFields()])
        return f"{DatabaseEnums.USER_TABLE.value}({fields_string})"

    def getFields(self) -> List[EntField]:
        return [EntField("name"), EntField("age")]

    def getEdges(self) -> List[EntEdge]:
        return [EntEdge(edge_name="Friends", edge_type=UserSchema, is_list=True)]
