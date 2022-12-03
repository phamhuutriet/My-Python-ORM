from unittest import TestCase
from unittest_data_provider import data_provider
from EntQuerier.Predicator import Predicator
from EntQuerier.EntQuerierBuilder import EntQuerierBuilder
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from typing import List


class TestEntQuerierBuilder(TestCase):
    def AndDataProvider():
        predicators_list = [
            [
                PredicatorBuilder.equalInt("age", 22),
                PredicatorBuilder.equalString("name", "Triet"),
            ],
            [
                PredicatorBuilder.equalInt("age", 22),
                PredicatorBuilder.equalString("name", "Triet"),
                PredicatorBuilder.equalString("title", "Software Engineer"),
            ],
        ]
        predicator_str_list = [
            '(age = 22) AND (name = "Triet")',
            '((age = 22) AND (name = "Triet")) AND (title = "Software Engineer")',
        ]
        return (
            (predicators, predicator_str)
            for predicators, predicator_str in zip(
                predicators_list, predicator_str_list
            )
        )

    @data_provider(AndDataProvider)
    def testAnd(self, predicators: List[Predicator], predicator_str: str):
        self.assertEqual(str(EntQuerierBuilder._and(*predicators)), predicator_str)

    def OrDataProvider():
        predicators_list = [
            [
                PredicatorBuilder.equalInt("age", 22),
                PredicatorBuilder.equalString("name", "Triet"),
            ],
            [
                PredicatorBuilder.equalInt("age", 22),
                PredicatorBuilder.equalString("name", "Triet"),
                PredicatorBuilder.equalString("title", "Software Engineer"),
            ],
        ]
        predicator_str_list = [
            '(age = 22) OR (name = "Triet")',
            '((age = 22) OR (name = "Triet")) OR (title = "Software Engineer")',
        ]
        return (
            (predicators, predicator_str)
            for predicators, predicator_str in zip(
                predicators_list, predicator_str_list
            )
        )

    @data_provider(OrDataProvider)
    def testOr(self, predicators: List[Predicator], predicator_str: str):
        self.assertEqual(str(EntQuerierBuilder._or(*predicators)), predicator_str)

    def NotDataProvider():
        predicator_list = [
            PredicatorBuilder.equalInt("age", 22),
            PredicatorBuilder.equalString("title", "Software Engineer"),
        ]
        predicator_str_list = ["NOT age = 22", 'NOT title = "Software Engineer"']
        return (
            (predicator, predicator_str)
            for predicator, predicator_str in zip(predicator_list, predicator_str_list)
        )

    @data_provider(NotDataProvider)
    def testNot(self, predicator: Predicator, predicator_str: str):
        self.assertEqual(str(EntQuerierBuilder._not(predicator)), predicator_str)

    def testCombineMethods(self):
        p1 = PredicatorBuilder.equalInt("age", 22)
        p2 = PredicatorBuilder.equalString("name", "Triet")
        p3 = PredicatorBuilder.equalString("title", "Software Engineer")
        predicator_str = f"(({str(p1)}) OR ({str(p2)})) AND ({str(p3)})"
        self.assertEqual(
            str(EntQuerierBuilder._and(EntQuerierBuilder._or(p1, p2), p3)),
            predicator_str,
        )
