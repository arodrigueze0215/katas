from Domain.User.user import User
class FollowUser(object):
    """docstring for followTo."""

    def __init__(self, User):
        self.user = User

    def follow(self, User):
        self.user.followUser(User)

    def isFollowing(self, User):
        if self.user.getFollowingUser(User) is None:
            return False
        else:
            return True
