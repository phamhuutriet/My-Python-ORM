from enums.DatabaseEnums import DatabaseEnums
import sqlite3


class MockDatabase:
    @staticmethod
    def initializeCursorAndConnection():
        """This method initialize the cursor and the connection of sqlite server"""
        connection = sqlite3.connect(DatabaseEnums.TEST_DATABASE_PATH.value)
        cursor = connection.cursor()
        connection.commit()
        return cursor, connection

    @staticmethod
    def dropTable(table_name: str) -> None:
        cursor, connection = MockDatabase.initializeCursorAndConnection()
        cursor.execute(f"DROP TABLE {table_name};")
        connection.commit()
        connection.close()

    @staticmethod
    def insertToTable(table_name, value):
        cursor, connection = MockDatabase.initializeCursorAndConnection()
        cursor.execute(f"INSERT INTO {table_name} VALUES ({value});")
        connection.commit()
        cursor.execute("SELECT last_insert_rowid();")
        connection.commit()
        id = cursor.fetchone()[0]
        connection.close()
        return id

    @staticmethod
    def createInsertValue(*args):
        str_args = [str(ele) for ele in args]
        return '"' + '","'.join(str_args) + '"'

    @staticmethod
    def isExistInTable(table_name: str, id: int, optional_condition: str = ""):
        """Check if an entity is existed in a table by checking its ID (by default),
        and with optional condition (null by default)
        Parameter:
            table_name: name of the table
            id: the id of the entity
            optional_condition: WHERE condition other than id
        """
        cursor, connection = MockDatabase.initializeCursorAndConnection()
        cursor.execute(
            f"SELECT * FROM {table_name} WHERE id = {id} {optional_condition};"
        )
        connection.commit()
        isExist = len(cursor.fetchall()) > 0
        connection.close()
        return isExist
