from EntQuerier.EntQuerierInterface import EntQuerierInterface
from EntSchema.EntSchemaInterface import EntSchemaInterface
from Ent.EntInterface import EntInterface
from demo.User.User import User
from demo.User.UserSchema import UserSchema


class UserQuerier(EntQuerierInterface):
    @staticmethod
    def processOneResult(result: dict) -> EntInterface:
        ent = User(name=result["name"], age=result["age"])
        ent.setID(result["id"])
        return ent

    @staticmethod
    def getEntSchema() -> EntSchemaInterface:
        return UserSchema()
