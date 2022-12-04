from EntQuerier.EntQuerierInterface import EntQuerierInterface
from EntSchema.EntSchemaInterface import EntSchemaInterface
from demo.User.User import User
from demo.User.UserMutator import UserMutator
from demo.User.UserSchema import UserSchema
from Ent.EntInterface import EntInterface
from typing import List


class UserQuerier(EntQuerierInterface):
    @staticmethod
    def processOneResult(result: dict) -> EntInterface:
        user = User()
        user.setName(result["name"])
        user.setAge(result["age"])
        user.setID(result["id"])
        return user

    @staticmethod
    def processManyResults(results: List[dict]) -> List[EntInterface]:
        return list(UserQuerier.processOneResult(result) for result in results)

    @staticmethod
    def getEntSchema() -> EntSchemaInterface:
        return UserSchema()
