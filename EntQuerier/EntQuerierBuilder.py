from EntQuerier.EntQueryFilter import EntQueryFilter
from EntQuerier.Predicator import Predicator
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from enums.PredicatorEnums import PredicatorEnums
from typing import List


class EntQuerierBuilder:
    def __init__(self, predicators: List[Predicator]) -> None:
        self.predicators = predicators

    def _and(self, predicators: List[Predicator]) -> Predicator:
        ans = predicators[0]
        for i in range(1, len(predicators)):
            ans = PredicatorBuilder.combinePredicators(
                ans, predicators[i], PredicatorEnums.AND
            )
        return ans

    def _or(self, predicators: List[Predicator]) -> Predicator:
        ans = predicators[0]
        for i in range(1, len(predicators)):
            ans = PredicatorBuilder.combinePredicators(
                ans, predicators[i], PredicatorEnums.OR
            )
        return ans

    def _not(self, predicator: Predicator) -> Predicator:
        predicator.is_not = True
        return predicator

    def where(self, predicator: Predicator) -> None:
        self.predicators.append(predicator)

    def build(self) -> EntQueryFilter:
        return EntQueryFilter(self.predicators)
