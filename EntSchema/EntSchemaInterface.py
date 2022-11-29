from abc import ABC, abstractmethod
from EntSchema.EntField import EntField
from EntSchema.EntEdge import EntEdge
from typing import List


class EntSchemaInterface(ABC):
    @abstractmethod
    def getFields() -> List[EntField]:
        pass

    @abstractmethod
    def getEdges() -> List[EntEdge]:
        pass
