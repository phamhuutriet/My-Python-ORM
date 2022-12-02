from __future__ import annotations
from abc import ABC, abstractmethod
from EntSchema.EntSchemaInterface import EntSchemaInterface
from typing import List


class EntInterface(ABC):
    @abstractmethod
    def getEntSchema(self) -> EntSchemaInterface:
        """Return the repsective schema of this entity"""

    @abstractmethod
    def getID(self) -> int:
        """Return the integer id of this entity"""

    @abstractmethod
    def setID(self, id: int) -> None:
        """Set the id of an ent"""

    def getFieldsNames(self) -> List[str]:
        """Return a list of fields names"""
        return list(field.getName() for field in self.getEntSchema().getFields())

    @abstractmethod
    def getEdges(self) -> dict[EntInterface, str]:
        """Return a dictionary with key is the edge name and value is an ent"""

    def toDict(self) -> dict:
        """Return a dict format of the ent, empty fields are included with Null values"""
        self_dict = self.__dict__
        return {
            field: self_dict[field] if field in self_dict else None
            for field in self.getFieldsNames()
        }
