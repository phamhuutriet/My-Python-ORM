from abc import ABC, abstractmethod
from EntSchema.EntSchemaInterface import EntSchemaInterface
from typing import List


class EntInterface(ABC):
    @abstractmethod
    def Create(self):
        return self

    @abstractmethod
    def Query(self):
        return self

    @abstractmethod
    def Update(self):
        return self

    @abstractmethod
    def Delete(self):
        return self

    @abstractmethod
    def getEntSchema(self) -> EntSchemaInterface:
        return

    @abstractmethod
    def getFieldsValues(self) -> List:
        """Return a list of values of every fields of this entity following its schema field order"""
        return
