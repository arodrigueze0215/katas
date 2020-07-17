from domain.post.post import Post
class PostMessage(object):
    """docstring for PostMessage."""

    def __init__(self, timelineRepository):
        self.timelineRepository = timelineRepository

    def execute(self, **kwarg):
        nickname = kwarg.get('nickname')
        message = kwarg.get('message')
        post = Post(message)
        self.timelineRepository.save(nickname, post)
