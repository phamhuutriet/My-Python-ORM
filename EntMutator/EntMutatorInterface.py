from Ent.EntInterface import EntInterface
from EntMutator.SQLHelper import SQLHelper


class EntMutatorInterface:
    @staticmethod
    def persist(ent: EntInterface) -> None:
        """This method create/update the ent in the database"""
        ent_schema = ent.getEntSchema()
        table_name = SQLHelper.constructEntSchemaInsertTableString(ent_schema)
        insert_value = SQLHelper.createInsertValue(ent.getFieldsValues())
        SQLHelper.insertToTable(table_name, insert_value)
