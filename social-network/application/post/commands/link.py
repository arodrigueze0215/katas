import re
class LinkSomething(object):

    def __init__(self, timelineRepository):
        self.timelineRepository = timelineRepository
        self.REGEX = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

    def execute(self, nickname, post):
        links= re.findall(self.REGEX, post.message)
        post.links = links
        self.timelineRepository.save(nickname, post)
