from abc import ABC, abstractmethod
from typing import List
from EntMutator.SQLHelper import SQLHelper
from EntSchema.EntSchemaInterface import EntSchemaInterface
from Ent.EntInterface import EntInterface
from EntQuerier.Predicator import Predicator


class EntQuerierInterface(ABC):
    def queryOne(self, filter: Predicator) -> EntInterface:
        """This method help queries one ent"""
        result = SQLHelper.queryOne(
            table_name=self.getEntSchema().getTableName(),
            filter_string=str(filter),
        )
        return self.processOneResult(result)

    def queryMany(self, filter: Predicator) -> List[EntInterface]:
        """This method help queries many ents"""
        results = SQLHelper.queryMany(
            table_name=self.getEntSchema().getTableName(),
            filter_string=str(filter),
        )
        return self.processManyResults(results)

    @abstractmethod
    def getEntSchema(self) -> EntSchemaInterface:
        """Return the ent schema type of this ent querier"""

    @abstractmethod
    def processOneResult(self, result: dict) -> EntInterface:
        """This method process the dict result and pass it to Ent class init"""

    @abstractmethod
    def processManyResults(self, results: List[dict]) -> List[EntInterface]:
        """This method process the list of dicts result and pass it to list of Ents"""
