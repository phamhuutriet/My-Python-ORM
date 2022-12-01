from Ent.EntInterface import EntInterface
from EntMutator.SQLHelper import SQLHelper
from abc import ABC
from typing import List


class EntMutatorInterface(ABC):
    @staticmethod
    def create(ent: EntInterface) -> None:
        EntMutatorInterface.createSingle(ent)
        EntMutatorInterface.createEdge(ent=ent, edges=ent.getEdges())

    @staticmethod
    def createSingle(ent: EntInterface) -> None:
        """This method create the ent in the database with no edges"""
        ent_schema = ent.getEntSchema()
        ent_ID = SQLHelper.insertToTable(
            table_name=ent_schema.getTableName(),
            inserted_value_str=SQLHelper.createInsertValue(ent.__dict__),
        )
        ent.setID(ent_ID)

    @staticmethod
    def createEdge(ent: EntInterface, edges: List[EntInterface]) -> None:
        """This method create the edge"""
        for edge in edges:
            EntMutatorInterface.createSingle(edge)
            EntMutatorInterface.insertRelationshipRecord(ent, edge)

    @staticmethod
    def insertRelationshipRecord(ent1: EntInterface, ent2: EntInterface) -> None:
        SQLHelper.insertToTable(
            table_name=SQLHelper.createRelationshipTableName(
                table_name1=ent1.getEntSchema().getTableName(),
                table_name2=ent2.getEntSchema().getTableName(),
            ),
            inserted_value_str=SQLHelper.createInsertValue(
                {"id1": ent1.getID(), "id2": ent2.getID()}
            ),
        )

    @staticmethod
    def update(ent: EntInterface) -> None:
        """This method update the ent in the database"""
        ent_schema = ent.getEntSchema()
        SQLHelper.updateToTable(
            table_name=ent_schema.getTableName(),
            updated_string=SQLHelper.createUpdateString(ent.__dict__),
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
