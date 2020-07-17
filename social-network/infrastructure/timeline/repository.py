from domain.post.post import Post
from domain.timeline.timeline import TimeLine

class Repository(object):
    def __init__(self):
        self.timeLine = TimeLine()
        self.timeLineList = {}


    def findPost(self, **params):
        timeline = self.timeLineList[params.get('nickname')]
        for post in timeline.posts:
            if post.message == params.get('message'):
                return post
        return None

    def findTimelineByNickname(self, nickname):
        timeline = self.timeLineList.get(nickname)
        return timeline

    def hasMentionedTo(self, **params):
        for mention in params.get('post').mentioned:
            if mention == f'@{params.get("nickname")}':
                return True
        return False

    def hasLink(self, **params):
        for link in params.get('post').links:
            if link == params.get("link"):
                return True
        return False

    def save(self, nickname, post):
        if nickname in self.timeLineList.keys():
            timeline = self.timeLineList[nickname]
            timeline.posts.append(post)
        else:
            self.timeLine.user = nickname
            self.timeLine.posts.append(post)
            self.timeLineList[nickname] = self.timeLine
