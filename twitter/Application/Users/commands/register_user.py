from Domain.User.user import User
from Domain.User.repository import Repository

class RegisterUser(object):

    def __init__(self, Repository):
        self.repository = Repository


    def execute(self, nickname):
        if nickname not in self.repository.userDic:
            user = User(nickname)
            self.repository.userDic[nickname] = user
        else:
            raise Exception('this user already exist')
