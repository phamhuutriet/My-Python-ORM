from enums.DatabaseEnums import DatabaseEnums
from Exceptions.DuplicateRecordError import DuplicateRecordError
from EntSchema.EntSchemaInterface import EntSchemaInterface
import sqlite3


class SQLHelper:
    @staticmethod
    def initializeCursorAndConnection():
        connection = sqlite3.connect(DatabaseEnums.DATABASE_PATH.value)
        cursor = connection.cursor()
        connection.commit()
        return cursor, connection

    @staticmethod
    def insertToTable(table_name: str, value: str) -> None:
        cursor, connection = SQLHelper.initializeCursorAndConnection()
        try:
            cursor.execute(f"INSERT INTO {table_name} VALUES ({value});")
            connection.commit()
        except:
            raise DuplicateRecordError
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
    def constructEntSchemaInsertTableString(ent_schema: EntSchemaInterface):
        columns = ",".join(list(field.getName() for field in ent_schema.getFields()))
        return f"{ent_schema.getTableName()}({columns})"
