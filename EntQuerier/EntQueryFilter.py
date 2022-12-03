from EntQuerier.Predicator import Predicator
from typing import List


class EntQueryFilter:
    def __init__(self, predicators: List[Predicator]) -> None:
        self.predicators = predicators

    def toSQLString(self) -> str:
        """This method convert the filter to condition SQL string"""
        return "AND " + "AND ".join(str(predicator) for predicator in self.predicators)
