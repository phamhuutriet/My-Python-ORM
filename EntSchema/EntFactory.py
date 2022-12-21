from EntSchema.EntSchemaInterface import EntSchemaInterface
from Ent.EntInterface import EntInterface
from Ent.NullEnt import NullEnt
from demo.User.UserSchema import UserSchema
from demo.User.User import User


class EntFactory:
    @staticmethod
    def buildEnt(schema: EntSchemaInterface) -> EntInterface:
        """Each schema generation will insert an if statement for its schema"""
        if isinstance(schema, UserSchema):
            return User()
        return NullEnt()
