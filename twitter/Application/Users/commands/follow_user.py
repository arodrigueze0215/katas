from Domain.User.user import User
from Domain.User.repository import Repository

class FollowUser(object):
    """docstring for followTo."""

    def __init__(self, Repository):
        self.repository = Repository

    def execute(self, User, userToFollow):
        userToFollow = self.repository.getUserById(userToFollow)
        user = self.repository.getUserById(User)
        self.repository.setFollowing(user, userToFollow)
