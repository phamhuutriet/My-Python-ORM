from EntQuerier.EntQuerierInterface import EntQuerierInterface
from EntSchema.EntSchemaInterface import EntSchemaInterface
from demo.User.User import User
from demo.User.UserSchema import UserSchema
from EntQuerier.Predicator import Predicator
from Ent.EntInterface import EntInterface
from EntQuerier.PredicatorBuilder import PredicatorBuilder
from typing import List


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
        owner_id: int,
        filter: Predicator = PredicatorBuilder.emptyFilter(),
    ) -> User:
        user = UserQuerier.queryOneEdge(
            owner_id=owner_id,
            edge=UserSchema(),
            filter=filter,
            relationship="Friends",
        )
        if isinstance(user, User):
            return user
        raise TypeError

    @staticmethod
    def getManyFriends(
        owner_id: int,
        filter: Predicator = PredicatorBuilder.emptyFilter(),
    ) -> List[User]:
        results = UserQuerier.queryManyEdges(
            owner_id=owner_id, edge=UserSchema(), filter=filter, relationship="Friends"
        )
        if all(isinstance(result, User) for result in results):
            return results
        raise TypeError
