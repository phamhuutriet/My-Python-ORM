from __future__ import annotations
from Ent.EntInterface import EntInterface
from EntSchema.EntSchemaInterface import EntSchemaInterface
from EntSchema.NullEntSchema import NullEntSchema


class NullEnt(EntInterface):
    def getEntSchema(self) -> EntSchemaInterface:
        return NullEntSchema()

    def getID(self) -> int:
        return -1

    def setID(self, id: int) -> None:
        pass

    def getEdges(self) -> dict[EntInterface, str]:
        return {}

    def __eq__(self, __o: EntInterface) -> bool:
        return self.getID() == __o.getID()

    def populateFields(self, data: dict) -> None:
        return
