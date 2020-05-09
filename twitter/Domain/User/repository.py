from .user import User
class Repository(object):
    """docstring for UserRepository."""
    def __init__(self):
        self.userDic={}


    def getUserById(self,nickname) -> User:
        return self.userDic[nickname]

    def setFollowing(self, user, userToFollow):
        user.followings[userToFollow.nickname] = userToFollow

    def getFollowing(self, user, userToFollowMe):
        return user.followings[userToFollowMe]
