from Domain.User.user import User
from Infrastructure.User.repository import Repository

class FollowUser(object):
    """docstring for followTo."""

    def __init__(self, Repository):
        self.repository = Repository

    def execute(self, User, userToFollow):
        user = self.repository.getUserById(User)
        try:
            uToFollow = self.repository.getUserById(userToFollow)
        except Exception:
            raise Exception(f'The user {nickname} does not exist')

        if user.nickname == uToFollow.nickname:
            raise Exception('you can not follow yourself')
        else:
            self.repository.setFollowing(user, uToFollow)
