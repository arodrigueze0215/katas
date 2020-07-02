import json
class Repository(object):
    """docstring for UserRepository."""
    def __init__(self):
        self.userDic={}
        self.userDicOb={}

    def _save(self, user):
        self.userDicOb[user.nickname] = json.dumps(user.__dict__)
        js = json.dumps(self.userDicOb)
        js.replace('\"', '')
        print(js)
        with open('/home/arodriguez/projects/katas/twitter/Infrastructure/database.json', 'w', encoding='utf-8') as fl:
            fl.write(js)


    def save(self, user):
        self.userDic[user.nickname] = user
        self._save(user)

    def getUserById(self,nickname):
        try:
            return self.userDic[nickname]
        except Exception:
            raise

    def setFollowing(self, user, userToFollow):
        if userToFollow.nickname in user.followings.keys():
            raise
        else:
            user.followings[userToFollow.nickname] = userToFollow.__dict__


    def getFollowing(self, user, userToFollowMe):
        return user.followings[userToFollowMe]
