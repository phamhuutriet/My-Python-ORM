from unittest import TestCase
from unittest_data_provider import data_provider
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from EntQuerier.Predicator import Predicator
from enums.PredicatorEnums import PredicatorEnums
from typing import List


class TestPredicator(TestCase):
    def predicatorBuilderEqualIntDataProvider():
        field_name_list = ["a", "B"]
        value_list = [10, 0]
        predicator_str_list = ["a = 10", "B = 0"]
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderEqualIntDataProvider)
    def testPredicatorBuilderEqualInt(
        self, field_name: str, value: int, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.equalInt(field_name, value)), predicator_str
        )

    def predicatorBuilderLowerThanIntDataProvider():
        field_name_list = ["a", "B"]
        value_list = [10, 0]
        predicator_str_list = ["a < 10", "B < 0"]
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderLowerThanIntDataProvider)
    def testPredicatorBuilderLowerThanInt(
        self, field_name: str, value: int, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.lowerThanInt(field_name, value)), predicator_str
        )

    def predicatorBuilderLowerThanOrEqualIntDataProvider():
        field_name_list = ["a", "B"]
        value_list = [10, 0]
        predicator_str_list = ["a <= 10", "B <= 0"]
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderLowerThanOrEqualIntDataProvider)
    def testPredicatorBuilderLowerThanOrEqualInt(
        self, field_name: str, value: int, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.lowerThanOrEqualInt(field_name, value)),
            predicator_str,
        )

    def predicatorBuilderGreaterThanIntDataProvider():
        field_name_list = ["a", "B"]
        value_list = [10, 0]
        predicator_str_list = ["a > 10", "B > 0"]
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderGreaterThanIntDataProvider)
    def testPredicatorBuilderGreaterThanInt(
        self, field_name: str, value: int, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.greaterThanInt(field_name, value)),
            predicator_str,
        )

    def predicatorBuilderGreaterThanOrEqualIntDataProvider():
        field_name_list = ["a", "B"]
        value_list = [10, 0]
        predicator_str_list = ["a >= 10", "B >= 0"]
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderGreaterThanOrEqualIntDataProvider)
    def testPredicatorBuilderGreaterThanOrEqualInt(
        self, field_name: str, value: int, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.greaterThanOrEqualInt(field_name, value)),
            predicator_str,
        )

    def predicatorBuilderInIntsDataProvider():
        field_name_list = ["a", "B"]
        values_list = [[1, 2, 3, 4], [0]]
        predicator_str_list = ["a IN (1,2,3,4)", "B IN (0)"]
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, values_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderInIntsDataProvider)
    def testPredicatorBuilderInInts(
        self, field_name: str, values: List[int], predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.inInts(field_name, values)),
            predicator_str,
        )

    def predicatorBuilderEqualStringDataProvider():
        field_name_list = ["a", "B"]
        value_list = ["A", "10"]
        predicator_str_list = ['a = "A"', 'B = "10"']
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderEqualStringDataProvider)
    def testPredicatorBuilderEqualString(
        self, field_name: str, value: str, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.equalString(field_name, value)), predicator_str
        )

    def predicatorBuilderLikeStringDataProvider():
        field_name_list = ["a", "B"]
        value_list = ["A", "10"]
        predicator_str_list = ['a LIKE "A"', 'B LIKE "10"']
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderLikeStringDataProvider)
    def testPredicatorBuilderLikeString(
        self, field_name: str, value: str, predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.likeString(field_name, value)), predicator_str
        )

    def predicatorBuilderInStringDataProvider():
        field_name_list = ["a", "B"]
        value_list = [["A", "10"], ["b"]]
        predicator_str_list = ['a IN ("A","10")', 'B IN ("b")']
        return (
            (field_name, value, predicator_str)
            for field_name, value, predicator_str in zip(
                field_name_list, value_list, predicator_str_list
            )
        )

    @data_provider(predicatorBuilderInStringDataProvider)
    def testPredicatorBuilderInString(
        self, field_name: str, values: List[str], predicator_str: str
    ):
        self.assertEqual(
            str(PredicatorBuilder.inStrings(field_name, values)), predicator_str
        )

    def combinePredicatorsDataProvider():
        p1_list = [
            PredicatorBuilder.equalInt("a", 5),
            PredicatorBuilder.equalInt("a", 5),
        ]
        p2_list = [
            PredicatorBuilder.equalString("b", "A"),
            PredicatorBuilder.equalString("b", "A"),
        ]
        relationship_list = [PredicatorEnums.AND, PredicatorEnums.OR]
        predicator_str_list = ['(a = 5) AND (b = "A")', '(a = 5) OR (b = "A")']
        return (
            (p1, p2, relationship, predicator_str)
            for p1, p2, relationship, predicator_str in zip(
                p1_list, p2_list, relationship_list, predicator_str_list
            )
        )

    @data_provider(combinePredicatorsDataProvider)
    def testCombinePredicators(
        self,
        p1: Predicator,
        p2: Predicator,
        relationship: PredicatorEnums,
        predicator_str: str,
    ):
        self.assertEqual(
            str(PredicatorBuilder.combinePredicators(p1, p2, relationship)),
            predicator_str,
        )
