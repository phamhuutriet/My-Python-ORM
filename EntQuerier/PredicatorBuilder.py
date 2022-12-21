from EntQuerier.Predicator import Predicator
from enums.PredicatorEnums import PredicatorEnums
from typing import List


class PredicatorBuilder:
    @staticmethod
    def equalInt(field_name: str, value: int) -> Predicator:
        return Predicator(field_name, PredicatorEnums.EQUAL, value)

    @staticmethod
    def lowerThanInt(field_name: str, value: int) -> Predicator:
        return Predicator(field_name, PredicatorEnums.LOWER_THAN, value)

    @staticmethod
    def lowerThanOrEqualInt(field_name: str, value: int) -> Predicator:
        return Predicator(field_name, PredicatorEnums.LOWER_THAN_OR_EQUAL, value)

    @staticmethod
    def greaterThanInt(field_name: str, value: int) -> Predicator:
        return Predicator(field_name, PredicatorEnums.GREATER_THAN, value)

    @staticmethod
    def greaterThanOrEqualInt(field_name: str, value: int) -> Predicator:
        return Predicator(field_name, PredicatorEnums.GREATER_THAN_OR_EQUAL, value)

    @staticmethod
    def inInts(field_name: str, values: List[int]) -> Predicator:
        return Predicator(field_name, PredicatorEnums.IN, values)

    @staticmethod
    def equalString(field_name: str, value: str) -> Predicator:
        return Predicator(field_name, PredicatorEnums.EQUAL, value)

    @staticmethod
    def likeString(field_name: str, value: str) -> Predicator:
        return Predicator(field_name, PredicatorEnums.LIKE, value)

    @staticmethod
    def inStrings(field_name: str, values: List[str]) -> Predicator:
        return Predicator(field_name, PredicatorEnums.IN, values)

    @staticmethod
    def combinePredicators(
        p1: Predicator, p2: Predicator, relationship: PredicatorEnums
    ) -> Predicator:
        p1.setNested()
        p2.setNested()
        return Predicator(p1, relationship, p2)

    @staticmethod
    def emptyFilter() -> Predicator:
        return Predicator("1", PredicatorEnums.EQUAL, 1)
