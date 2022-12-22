from EntMutator.EntMutatorInterface import EntMutatorInterface
from demo.User.User import User


class UserMutator(EntMutatorInterface):
    @staticmethod
    def removeFriend(user: User, friend: User) -> None:
        UserMutator.deleteEdge(ent=user, edge=friend, relationship="Friends")
        user.removeFriend(friend)
