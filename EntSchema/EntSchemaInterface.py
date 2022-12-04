from abc import ABC, abstractmethod
from EntSchema.EntField import EntField
from EntSchema.EntEdge import EntEdge
from enums.DatabaseEnums import DatabaseEnums
from typing import List


class EntSchemaInterface(ABC):
    def getTableName(self, show_fields: bool = False) -> str:
        """Return the table name that stores this entity
        Parameters:
            show_fields (bool): if show the field columns in table name.
            Example: User(name, age) vs User
        """
        if not show_fields:
            return self.tableName().value
        fields_string = ",".join([field.getName() for field in self.getFields()])
        return f"{self.tableName().value}({fields_string})"

    @abstractmethod
    def tableName(self) -> DatabaseEnums:
        """Define the table name as a string here"""

    @abstractmethod
    def getFields(self) -> List[EntField]:
        """Configure the fields of this entity"""

    @abstractmethod
    def getEdges(self) -> List[EntEdge]:
        """Configure the edges of this entity"""

    def getFieldsNames(self) -> List[str]:
        return list(field.getName() for field in self.getFields())
