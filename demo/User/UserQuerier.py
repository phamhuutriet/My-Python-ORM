from EntQuerier.EntQuerierInterface import EntQuerierInterface
from EntSchema.EntSchemaInterface import EntSchemaInterface
from demo.User.User import User
from demo.User.UserSchema import UserSchema
from EntQuerier.Predicator import Predicator
from Ent.EntInterface import EntInterface
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from EntMutator.SQLHelper import SQLHelper


class UserQuerier(EntQuerierInterface):
    @staticmethod
    def processOneResult(result: dict) -> User:
        ent = User(name=result["name"], age=result["age"])
        ent.setID(result["id"])
        return ent

    @staticmethod
    def getEntSchema() -> EntSchemaInterface:
        return UserSchema()

    @staticmethod
    def getOneFriend(
        filter: Predicator = PredicatorBuilder.emptyFilter(),
    ) -> EntInterface:
        return UserQuerier.queryOneEdge(
            edge=UserSchema(),
            filter=filter,
            relationship="Friends",
        )
