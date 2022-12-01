from enums.DatabaseEnums import DatabaseEnums
from Exceptions.DuplicateRecordError import DuplicateRecordError
import sqlite3


class SQLHelper:
    @staticmethod
    def initializeCursorAndConnection():
        """This method initialize the cursor and the connection of sqlite server"""
        connection = sqlite3.connect(DatabaseEnums.DATABASE_PATH.value)
        cursor = connection.cursor()
        connection.commit()
        return cursor, connection

    @staticmethod
    def insertToTable(table_name: str, inserted_value_str: str) -> int:
        """This method help insert a VALUE into a table
        Parameter:
            table_name: the name of the table we want to insert
            inserted_value_str: the string contains the inserted value in the form of VALUE in SQL
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        try:
            cursor.execute(f"INSERT INTO {table_name} VALUES ({inserted_value_str});")
            connection.commit()
        except:
            raise DuplicateRecordError
        cursor.execute("SELECT last_insert_rowid();")
        connection.commit()
        id = cursor.fetchone()[0]
        connection.close()
        return id

    @staticmethod
    def createInsertValue(values_dict: dict):
        """This method helps to create an inserted value string in the form of VALUE in SQL
        Parameter:
            values_dict (dict): a dictionary with key is a field name and value is the value of that field
        """
        str_args = [str(value) for value in values_dict.values()]
        return '"' + '","'.join(str_args) + '"'

    @staticmethod
    def updateToTable(table_name: str, updated_string: str) -> None:
        """This method helps to update an existed record in the database
        Parameter:
            table_name: the table we want to update
            updated_string: the string contains the updated value in the form of SET in SQL
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        sql = f"""UPDATE {table_name}
                  SET {updated_string};
               """
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @staticmethod
    def createUpdateString(update_dict: dict) -> str:
        """A method help to create an update string in SQL.
        Parameters:
            update_dict (dict): a dictionary with key is a field name and value is the value of that field
        """
        return ",".join([f"{key} = {value}" for key, value in update_dict.items()])

    @staticmethod
    def deleteRecordFromTable(table_name: str, record_id: int) -> None:
        """This method deletes a record from a table
        Parameter:
            table_name: the table we want to delete a record
            record_id: the id of the record
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        sql = f"DELETE FROM {table_name} WHERE id = {record_id};"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @staticmethod
    def isExistInTable(table_name: str, record_id: int) -> bool:
        """This method checks if the record is in the table
        Parameter:
            table_name: the table we want to check on
            record_id: the id of the record we want to check
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        sql = f"SELECT 1 FROM {table_name} WHERE id = {record_id};"
        cursor.execute(sql)
        connection.commit()
        is_existed = cursor.fetchone()[0] == 1
        connection.close()
        return is_existed

    @staticmethod
    def createRelationshipTableName(table_name1: str, table_name2: str) -> str:
        return f"{table_name1}_{table_name2}({table_name1}, {table_name2})"
