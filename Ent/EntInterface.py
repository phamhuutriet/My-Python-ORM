from abc import ABC, abstractmethod
from EntSchema.EntSchemaInterface import EntSchemaInterface
from typing import List
from __future__ import annotations


class EntInterface(ABC):
    @abstractmethod
    def getEntSchema(self) -> EntSchemaInterface:
        """Return the repsective schema of this entity"""
        return

    def getFieldsNames(self) -> List[str]:
        """Return a list of fields names"""
        return list(field.getName() for field in self.getEntSchema().getFields())

    def getEdges(self) -> List[EntInterface]:
        return []

    @abstractmethod
    def getID(self) -> int:
        """Return the integer id of this entity"""
        pass

    @abstractmethod
    def setID(self, id: int) -> None:
        pass

    def toDict(self) -> dict:
        """Return a dict format of the ent, empty fields are included with Null values"""
        self_dict = self.__dict__
        return {
            field: self_dict[field] if field in self_dict else None
            for field in self.getFieldsNames()
        }
