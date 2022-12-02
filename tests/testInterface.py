from unittest import TestCase
from unittest.mock import patch
from enums.DatabaseEnums import DatabaseEnums
from tests.MockDatabase import MockDatabase


class TestInterface(TestCase):
    @patch("EntMutator.SQLHelper.SQLHelper.getDatabasePath")
    def setUp(self, mocked_get_path) -> None:
        mocked_get_path.return_value = DatabaseEnums.TEST_DATABASE_PATH.value
