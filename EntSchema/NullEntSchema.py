from EntSchema.EntSchemaInterface import EntSchemaInterface
from EntSchema.EntField import EntField
from EntSchema.EntEdge import EntEdge
from enums.DatabaseEnums import DatabaseEnums
from typing import List


class NullEntSchema(EntSchemaInterface):
    def __init__(self) -> None:
        super().__init__()

    def getTableName(self, show_fields: bool = False) -> str:
        return ""

    def getFields(self) -> List[EntField]:
        return []

    def getEdges(self) -> List[EntEdge]:
        return []

    def tableName(self) -> DatabaseEnums:
        return DatabaseEnums.NULL
