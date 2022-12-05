from EntSchema.EntSchemaInterface import EntSchemaInterface
from EntSchema.EntField import EntField
from EntSchema.EntFieldBuilder import EntFieldBuilder
from EntSchema.EntEdge import EntEdge
from enums.DatabaseEnums import DatabaseEnums
from enums.EntFieldEnums import EntFieldEnums
from typing import List


class UserSchema(EntSchemaInterface):
    def __init__(self) -> None:
        pass

    def tableName(self) -> DatabaseEnums:
        return DatabaseEnums.USER_TABLE

    def getFields(self) -> List[EntField]:
        return [
            EntFieldBuilder.field()
            .name("name")
            .unique()
            .type(EntFieldEnums.STRING)
            .build(),
            EntFieldBuilder.field().name("age").type(EntFieldEnums.INT).build(),
        ]

    def getEdges(self) -> List[EntEdge]:
        return [EntEdge(edge_name="Friends", edge_type=UserSchema, is_list=True)]
