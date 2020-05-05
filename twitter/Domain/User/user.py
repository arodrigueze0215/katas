class User(object):
    """docstring for User."""
    followings = list()

    def __init__(self, nickname):
        self.nickname = nickname

    def followUser(self,User):
        self.followings.append(User)

    def getFollowingUser(self, User):
         if User in self.followings:
             return User
