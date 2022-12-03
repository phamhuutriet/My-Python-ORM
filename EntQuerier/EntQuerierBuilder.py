from EntQuerier.Predicator import Predicator
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from enums.PredicatorEnums import PredicatorEnums
from typing import List


class EntQuerierBuilder:
    @staticmethod
    def _and(*predicators) -> Predicator:
        ans = predicators[0]
        for i in range(1, len(predicators)):
            ans = PredicatorBuilder.combinePredicators(
                ans, predicators[i], PredicatorEnums.AND
            )
        return ans

    @staticmethod
    def _or(*predicators) -> Predicator:
        ans = predicators[0]
        for i in range(1, len(predicators)):
            ans = PredicatorBuilder.combinePredicators(
                ans, predicators[i], PredicatorEnums.OR
            )
        return ans

    @staticmethod
    def _not(predicator: Predicator) -> Predicator:
        predicator.is_not = True
        return predicator
