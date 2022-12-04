from unittest import TestCase
from unittest.mock import patch, MagicMock
from unittest_data_provider import data_provider
from enums.DatabaseEnums import DatabaseEnums
from tests.MockDatabase import MockDatabase
from EntMutator.SQLHelper import SQLHelper
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from EntQuerier.EntQuerierBuilder import EntQuerierBuilder
from Ent.NullEnt import NullEnt
from demo.User.UserMutator import UserMutator
from demo.User.UserQuerier import UserQuerier
from demo.User.User import User
from typing import List

const_user = User()


class TestUser(TestCase):
    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def setUp(self, mocked_get_path: MagicMock) -> None:
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        # Main table
        SQLHelper.createTable(
            table_name=const_user.getEntSchema().getTableName(),
            table_description="id integer, name integer, age integer, PRIMARY KEY (id)",
        )
        # Relationship table
        SQLHelper.createTable(
            table_name=f"{const_user.getEntSchema().getTableName()}_Friends",
            table_description="USER integer, Friends integer",
        )

    def tearDown(self) -> None:
        MockDatabase.dropTable(const_user.getEntSchema().getTableName())
        MockDatabase.dropTable(f"{const_user.getEntSchema().getTableName()}_Friends")

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testCreateSingle(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        user = User(name="Triet", age=24)
        UserMutator.create(user)
        self.assertTrue(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(), id=user.getID()
            )
        )

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testCreateEdge(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        # Set up user and friends
        user = User(name="Triet", age=24)
        friend1 = User(name="friend1", age=10)
        friend2 = User(name="friend2", age=20)
        user.addFriend(friend=friend1)
        user.addFriend(friend=friend2)
        UserMutator.create(user)

        # Test if user existed
        self.assertTrue(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(), id=user.getID()
            )
        )
        # Test if friends existed
        for friend in user.getFriends():
            self.assertTrue(
                MockDatabase.isExistInTable(
                    table_name=friend.getEntSchema().getTableName(), id=friend.getID()
                )
            )

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testUpdate(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        user = User(name="Triet", age=24)
        UserMutator.create(user)
        user.setName("Mai")
        UserMutator.update(user)
        self.assertTrue(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(),
                id=user.getID(),
                optional_condition='AND name="Mai"',
            )
        )

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testDelete(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        user = User(name="Triet", age=24)
        # Test if user existed
        UserMutator.create(user)
        self.assertTrue(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(), id=user.getID()
            )
        )

        # Test if user is not existed
        UserMutator.delete(user)
        self.assertFalse(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(), id=user.getID()
            )
        )

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testIsExisted(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        user = User(name="Triet", age=23)
        self.assertFalse(UserMutator.isExisted(user))
        UserMutator.create(user)
        self.assertTrue(UserMutator.isExisted(user))

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testPersist(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        user = User(name="Triet", age=22)

        # Test if user existed
        UserMutator.persist(user)
        self.assertTrue(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(), id=user.getID()
            )
        )

        # Test if update successfully
        user.setName("Mai")
        user.setAge(23)
        UserMutator.persist(user)
        self.assertTrue(
            MockDatabase.isExistInTable(
                table_name=user.getEntSchema().getTableName(),
                id=user.getID(),
                optional_condition='AND name="Mai" AND age=23',
            )
        )

    def processOneResultDataProvider():
        result_list = [{"name": "Triet", "age": 23, "id": 1}]
        user_list = [User("Triet", 23)]
        return ((result, user) for result, user in zip(result_list, user_list))

    @data_provider(processOneResultDataProvider)
    def testProcessOneResult(self, result: dict, user: User):
        user.setID(result["id"])
        self.assertEqual(UserQuerier.processOneResult(result), user)

    def processManyResultsDataProvider():
        results_list = [
            [
                {"name": "Triet", "age": 23, "id": 1},
                {"name": "Triets", "age": 24, "id": 2},
                {"name": "Trit", "age": 22, "id": 3},
            ]
        ]
        users_list = [[User("Triet", 23), User("Triets", 24), User("Trit", 22)]]
        return ((results, users) for results, users in zip(results_list, users_list))

    @data_provider(processManyResultsDataProvider)
    def testProcessManyResults(self, results: List[dict], users: List[User]):
        for i in range(len(users)):
            users[i].setID(results[i]["id"])
        self.assertEqual(UserQuerier.processManyResults(results), users)

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testQueryOne(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        user = User("Triet", 23)
        UserMutator.create(user)

        # Query by name
        filter = PredicatorBuilder.equalString(field_name="name", value="Triet")
        self.assertEqual(UserQuerier.queryOne(filter), user)

        # Query by age
        filter = PredicatorBuilder.equalInt(field_name="age", value=23)
        self.assertEqual(UserQuerier.queryOne(filter), user)

        # Query by name and age
        filter = EntQuerierBuilder._and(
            PredicatorBuilder.equalString(field_name="name", value="Triet"),
            PredicatorBuilder.equalInt(field_name="age", value=23),
        )
        self.assertEqual(UserQuerier.queryOne(filter), user)

        # Cant find record
        filter = PredicatorBuilder.lowerThanInt(field_name="age", value=22)
        self.assertEqual(UserQuerier.queryOne(filter), NullEnt())

    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def testQueryMany(self, mocked_get_path: MagicMock):
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
        users = [User("Triet", 23), User("Mai", 24), User("Tram", 22)]
        for user in users:
            UserMutator.create(user)
        users.sort(key=lambda x: x.getID())

        # Query by name
        filter = PredicatorBuilder.inStrings("name", ["Triet", "Mai", "Tram"])
        results = sorted(UserQuerier.queryMany(filter), key=lambda x: x.getID())
        self.assertEqual(results, users)

        # Cant find records
        filter = PredicatorBuilder.equalInt("age", 200)
        results = sorted(UserQuerier.queryMany(filter), key=lambda x: x.getID())
        self.assertEqual(results, [NullEnt()])
