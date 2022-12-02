from Ent.EntInterface import EntInterface
from EntMutator.SQLHelper import SQLHelper
from abc import ABC
from typing import List


class EntMutatorInterface(ABC):
    @staticmethod
    def create(ent: EntInterface) -> None:
        """This method creates the ent and its edges"""
        EntMutatorInterface.createSingle(ent)
        EntMutatorInterface.createEdge(ent=ent, edges=ent.getEdges())

    @staticmethod
    def createSingle(ent: EntInterface) -> None:
        """This method create the ent in the database with no edges"""
        ent_schema = ent.getEntSchema()
        ent_ID = SQLHelper.insertToTable(
            table_name=ent_schema.getTableName(show_fields=True),
            inserted_value_str=SQLHelper.createInsertValue(ent.toDict()),
        )
        ent.setID(ent_ID)

    @staticmethod
    def createEdge(ent: EntInterface, edges: dict[EntInterface, str]) -> None:
        """This method create the edge"""
        for edge_object, edge_name in edges.items():
            EntMutatorInterface.createSingle(edge_object)
            EntMutatorInterface.insertRelationshipRecord(
                ent=ent, edge=edge_object, relationship=edge_name
            )

    @staticmethod
    def insertRelationshipRecord(
        ent: EntInterface, edge: EntInterface, relationship: str
    ) -> None:
        SQLHelper.insertToTable(
            table_name=f"{ent.getEntSchema().getTableName()}_{relationship}",
            inserted_value_str=SQLHelper.createInsertValue(
                {"id1": ent.getID(), "id2": edge.getID()}
            ),
        )

    @staticmethod
    def update(ent: EntInterface) -> None:
        """This method update the ent in the database"""
        ent_schema = ent.getEntSchema()
        SQLHelper.updateToTable(
            table_name=ent_schema.getTableName(),
            updated_string=SQLHelper.createUpdateString(ent.toDict()),
            id=ent.getID(),
        )

    @staticmethod
    def delete(ent: EntInterface) -> None:
        """This method delete the ent in the database"""
        SQLHelper.deleteRecordFromTable(
            table_name=ent.getEntSchema().getTableName(), record_id=ent.getID()
        )

    @staticmethod
    def isExisted(ent: EntInterface) -> bool:
        """This method checks if the ent is already existed in the database"""
        return SQLHelper.isExistInTable(
            table_name=ent.getEntSchema().getTableName(), record_id=ent.getID()
        )

    @staticmethod
    def persist(ent: EntInterface) -> None:
        """This method creates/updates the ent if it not existed/existed in the database"""
        if EntMutatorInterface.isExisted(ent):
            EntMutatorInterface.update(ent)
        else:
            EntMutatorInterface.create(ent)
