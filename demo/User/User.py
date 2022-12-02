from __future__ import annotations
from Ent.EntInterface import EntInterface
from EntSchema.EntSchemaInterface import EntSchemaInterface
from demo.User.UserSchema import UserSchema
from typing import List


class User(EntInterface):
    def __init__(self, name: str = "", age: int = 0) -> None:
        self.id = 0
        self.schema = UserSchema()
        self.name = name
        self.age = age
        self.friends = []

    def getEntSchema(self) -> EntSchemaInterface:
        return self.schema

    def getID(self) -> int:
        return self.id

    def setID(self, id: int) -> None:
        self.id = id

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getAge(self) -> int:
        return self.age

    def setAge(self, age: int) -> None:
        self.age = age

    def addFriend(self, friend: User) -> None:
        self.friends.append(friend)

    def getFriends(self) -> List[User]:
        return self.friends

    def getEdges(self) -> dict[EntInterface, str]:
        # Must have a generalized conversion
        return {friend: "Friends" for friend in self.friends}
