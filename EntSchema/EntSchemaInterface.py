from abc import ABC, abstractmethod
from EntSchema.EntField import EntField
from EntSchema.EntEdge import EntEdge
from typing import List


class EntSchemaInterface(ABC):
    @abstractmethod
    def getTableName(self, show_fields: bool = False) -> str:
        """Return the table name that stores this entity
        Parameters:
            show_fields (bool): if show the field columns in table name.
            Example: User(name, age) vs User
        """

    @abstractmethod
    def getFields(self) -> List[EntField]:
        """Configure the fields of this entity"""

    @abstractmethod
    def getEdges(self) -> List[EntEdge]:
        """Configure the edges of this entity"""
