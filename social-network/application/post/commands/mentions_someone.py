import re
class MentionsSomeone(object):

    def __init__(self, timelineRepository):
        self.timelineRepository = timelineRepository

    def execute(self, nickname, post):
        list_mentioned= re.findall("@\w+", post.message)
        post.mentioned = list_mentioned
        self.timelineRepository.save(nickname, post)
