from Domain.User.user import User

class RegisterUser(object):
    userDic={}

    def register(self, nickname):
        if nickname not in self.userDic:
            user = User(nickname)
            self.userDic[nickname] = user
        else:
            raise Exception('this user already exist')

    def getUserRegistered(self, nickname):
        return self.userDic[nickname]
