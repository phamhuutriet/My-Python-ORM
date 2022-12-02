from unittest import TestCase
from unittest.mock import patch, MagicMock
from enums.DatabaseEnums import DatabaseEnums
from tests.MockDatabase import MockDatabase
from EntMutator.SQLHelper import SQLHelper
from demo.User.UserMutator import UserMutator
from demo.User.User import User

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
        print(user.getEdges())
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
