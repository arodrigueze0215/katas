from Infrastructure.User.repository import Repository
class IsFollowing(object):
    """docstring for isFollowing."""

    def __init__(self, Repository):
        self.repository = Repository

    def execute(self, me, userToFollowMe):
        me = self.repository.getUserById(me)
        userToFollowMe = self.repository.getUserById(userToFollowMe)
        isFollowingMe = self.repository.getFollowing(me, userToFollowMe.nickname)
        return False if isFollowingMe == None else True
