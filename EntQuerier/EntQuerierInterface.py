from abc import ABC, abstractmethod
from Exceptions.NoRecordFound import NoRecordError
from typing import List
from EntMutator.SQLHelper import SQLHelper
from EntSchema.EntSchemaInterface import EntSchemaInterface
from Ent.EntInterface import EntInterface
from Ent.NullEnt import NullEnt
from EntQuerier.Predicator import Predicator
from EntSchema.EntFactory import EntFactory


class EntQuerierInterface(ABC):
    @classmethod
    def queryOne(cls, filter: Predicator) -> EntInterface:
        """This method help queries one ent"""
        try:
            result = SQLHelper.queryOne(
                table_name=cls.getEntSchema().getTableName(),
                filter_string=str(filter),
                fields=cls.getFieldsNames(),
            )
            return cls.processOneResult(result)
        except NoRecordError:
            return NullEnt()

    @classmethod
    def queryMany(cls, filter: Predicator) -> List[EntInterface]:
        """This method help queries many ents"""
        try:
            results = SQLHelper.queryMany(
                table_name=cls.getEntSchema().getTableName(),
                filter_string=str(filter),
                fields=cls.getFieldsNames(),
            )
            return cls.processManyResults(results)
        except NoRecordError:
            return [NullEnt()]

    @classmethod
    def queryOneEdge(
        cls,
        owner_id: int,
        edge: EntSchemaInterface,
        filter: Predicator,
        relationship: str,
    ) -> EntInterface:
        """This method help queries edge specifically"""
        try:
            result = SQLHelper.queryOneEdge(
                main_table_name=cls.getEntSchema().getTableName(),
                owner_id=owner_id,
                edge=relationship,
                filter_string=str(filter),
                fields=edge.getFieldsNames() + ["id"],
            )
            return cls.processEdge(edge, result)
        except NoRecordError:
            return NullEnt()

    @classmethod
    def queryManyEdges(
        cls,
        owner_id: int,
        edge: EntSchemaInterface,
        filter: Predicator,
        relationship: str,
    ) -> List[EntInterface]:
        try:
            results = SQLHelper.queryManyEdges(
                main_table_name=cls.getEntSchema().getTableName(),
                owner_id=owner_id,
                edge=relationship,
                filter_string=str(filter),
                fields=edge.getFieldsNames() + ["id"],
            )
            return cls.processManyEdges(results, edge)
        except NoRecordError:
            return [NullEnt()]

    @classmethod
    def processEdge(cls, edge: EntSchemaInterface, result: dict) -> EntInterface:
        """This method pass the result into an edge object"""
        ent = EntFactory.buildEnt(schema=edge)
        ent.populateFields(result)
        return ent

    @classmethod
    def processManyEdges(
        cls, results: List[dict], edge: EntSchemaInterface
    ) -> List[EntInterface]:
        return list(cls.processEdge(edge, result) for result in results)

    @staticmethod
    @abstractmethod
    def getEntSchema() -> EntSchemaInterface:
        """Return the ent schema type of this ent querier"""

    @staticmethod
    @abstractmethod
    def processOneResult(result: dict) -> EntInterface:
        """This method process the dict result and pass it to Ent class init"""

    @classmethod
    def processManyResults(cls, results: List[dict]) -> List[EntInterface]:
        """This method process the list of dicts result and pass it to list of Ents"""
        return list(cls.processOneResult(result) for result in results)

    @classmethod
    def getFieldsNames(cls) -> List[str]:
        return cls.getEntSchema().getFieldsNames() + ["id"]
