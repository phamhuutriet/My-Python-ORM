from abc import ABC, abstractmethod
from typing import List
from EntQuerier.EntQueryFilter import EntQueryFilter
from EntMutator.SQLHelper import SQLHelper
from EntSchema.EntSchemaInterface import EntSchemaInterface
from Ent.EntInterface import EntInterface


class EntQuerierInterface(ABC):
    def queryOne(self, filter: EntQueryFilter) -> EntInterface:
        """This method help queries one ent"""
        result = SQLHelper.queryOne(
            table_name=self.getEntSchema().getTableName(),
            filter_string=filter.toSQLString(),
        )
        return self.processOneResult(result)

    def queryMany(self, filter: EntQueryFilter) -> List[EntInterface]:
        """This method help queries many ents"""
        results = SQLHelper.queryMany(
            table_name=self.getEntSchema().getTableName(),
            filter_string=filter.toSQLString(),
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
