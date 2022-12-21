from enums.DatabaseEnums import DatabaseEnums
from typing import List
from Exceptions.NoRecordFound import NoRecordError
from EntSchema.EntSchemaInterface import EntSchemaInterface
import sqlite3


class SQLHelper:
    @staticmethod
    def getDatabasePath() -> str:
        return DatabaseEnums.DATABASE_PATH.value

    @staticmethod
    def createRelationshipTableString(
        schema: EntSchemaInterface, relationship: str
    ) -> str:
        return f"{schema.getTableName()}_{relationship}"

    @staticmethod
    def initializeCursorAndConnection():
        """This method initialize the cursor and the connection of sqlite server"""
        connection = sqlite3.connect(SQLHelper.getDatabasePath())
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
        sql = f"INSERT INTO {table_name} VALUES ({inserted_value_str});"
        cursor.execute(sql)
        connection.commit()
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
    def updateToTable(table_name: str, updated_string: str, id: int) -> None:
        """This method helps to update an existed record in the database
        Parameter:
            table_name: the table we want to update
            updated_string: the string contains the updated value in the form of SET in SQL
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        sql = f"""UPDATE {table_name}
                  SET {updated_string}
                  WHERE id = {id};
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
        strings = []
        for key, value in update_dict.items():
            if isinstance(value, str):
                strings.append(f'{key} = "{value}"')
            else:
                strings.append(f"{key} = {value}")
        return ",".join(strings)

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
        sql = f"SELECT * FROM {table_name} WHERE id = {record_id};"
        cursor.execute(sql)
        connection.commit()
        is_existed = len(cursor.fetchall()) == 1
        connection.close()
        return is_existed

    @staticmethod
    def createTable(table_name: str, table_description: str) -> None:
        """This methods create a table in the database
        Parameters:
            table_name: the name of the table
            table_description: the constraint string inside the create table parenthesese
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        cursor.execute(
            f"""CREATE TABLE {table_name} (
                        {table_description}
        );"""
        )
        connection.commit()
        connection.close()

    @staticmethod
    def createTableFieldsString(fields: List[str]) -> str:
        return ", ".join(fields)

    @staticmethod
    def queryOne(table_name: str, filter_string: str, fields: List[str]) -> dict:
        """This method queries one result based on table name and filter string
        Parameters:
            table_name: the name of the table
            filter_string: the SQL string for the conditional check (after WHERE)
        Return:
            a single dict contain one fetched result
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        sql = f"SELECT {SQLHelper.createTableFieldsString(fields)} FROM {table_name} WHERE {filter_string};"
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        connection.close()
        if not result:
            raise NoRecordError
        ans = {}
        for key, value in zip(fields, result):
            ans[key] = value
        return ans

    @staticmethod
    def queryMany(table_name: str, filter_string: str, fields: List[str]) -> List[dict]:
        """This method queries a list of results based on table name and filter string
        Parameters:
            table_name: the name of the table
            filter_string: the SQL string for the conditional check (after WHERE)
        Return:
            a list of dicts contain many fetched results
        """
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        sql = f"SELECT {SQLHelper.createTableFieldsString(fields)} FROM {table_name} WHERE {filter_string};"
        cursor.execute(sql)
        connection.commit()
        ans = list(cursor.fetchall())
        connection.close()
        if len(ans) == 0:
            raise NoRecordError
        for i, result in enumerate(ans):
            record = {}
            for key, value in zip(fields, result):
                record[key] = value
            ans[i] = record
        return ans

    @staticmethod
    def queryOneEdge(
        main_table_name: str,
        edge: str,
        filter_string: str,
        fields: List[str],
    ) -> dict:
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        relationship_table = f"{main_table_name}_{edge}"
        sql = f"""SELECT {SQLHelper.createTableFieldsString(fields)}
                  FROM {main_table_name} JOIN {relationship_table} 
                  ON {main_table_name}.id = {relationship_table}.{edge}
                  WHERE {filter_string};
                """
        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchone()
        connection.close()
        if not result:
            raise NoRecordError
        ans = {}
        for key, value in zip(fields, result):
            ans[key] = value
        return ans
