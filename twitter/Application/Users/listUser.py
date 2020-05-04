from .user import User

class List(object):
    list=list()
    def add(self, User):
        if User not in self.list:
            self.list.append(User)
        else:
            raise Exception('this user already exist')