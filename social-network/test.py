import unittest
from infrastructure.timeline.repository import Repository as TimelineRepository
from infrastructure.subscription.repository import Repository as SubscriptionRepository
from application.post.commands.post_message import PostMessage
from application.post.commands.mentions_someone import MentionsSomeone
from application.timeline.query.view_timeline import ViewTimeline
from application.subscribe.command.subscribe import Subscribe
from application.post.commands.link import LinkSomething

class TestSocialNetwork_Posting(unittest.TestCase):

    def setUp(self):
        self.timelineRepository = TimelineRepository()
        self.postMessage = PostMessage(self.timelineRepository)

    def test_can_publish_message_personal_timeline(self):
        self.postMessage.execute(nickname='arodriguez', message='hello first post')
        resultPostMessage = self.timelineRepository.findPost(nickname='arodriguez',message='hello first post')
        self.assertEqual(resultPostMessage.message, 'hello first post')


class TestSocialNetwork_Reading(unittest.TestCase):

    def setUp(self):
        self.timelineRepository = TimelineRepository()
        self.postMessage = PostMessage(self.timelineRepository)
        self.viewTimeline = ViewTimeline(self.timelineRepository)

    def test_can_view_timeline(self):
        self._post_three_message()
        timeLine = self.viewTimeline.execute(nickname='rafa')
        self._it_has_posts_on_timeline(timeLine.posts)

    def _it_has_posts_on_timeline(self, posts):
        self.assertEqual(posts[0].message, 'first post message')
        self.assertEqual(posts[1].message, 'second post message')
        self.assertEqual(posts[2].message, 'third post message')

    def _post_three_message(self):
        self.postMessage.execute(nickname='rafa', message='first post message')
        self.postMessage.execute(nickname='rafa', message='second post message')
        self.postMessage.execute(nickname='rafa', message='third post message')

class TestSocialNetwork_Following(unittest.TestCase):

    def setUp(self):
        self.timelineRepository = TimelineRepository()
        self.subscriptionRepository = SubscriptionRepository()
        self.viewTimeline = ViewTimeline(self.timelineRepository)
        self.subscribe = Subscribe(self.timelineRepository, self.subscriptionRepository)
        self.postMessage = PostMessage(self.timelineRepository)

    def test_subscribe_to_timeline(self):
        self._post_three_message('rafa')
        timeLine = self.viewTimeline.execute(nickname='rafa')
        self._post_three_message('arodriguez')
        timeLine = self.viewTimeline.execute(nickname='arodriguez')
        self.subscribe.execute(nickname='rafa')
        self.subscribe.execute(nickname='arodriguez')
        subscriptions_list = self.subscriptionRepository.listAllSubscriptions()
        self.assertEqual(subscriptions_list['rafa'].user,'rafa')
        self.assertEqual(subscriptions_list['arodriguez'].user,'arodriguez')

    def _post_three_message(self, to):
        self.postMessage.execute(nickname=to, message='first post message')
        self.postMessage.execute(nickname=to, message='second post message')
        self.postMessage.execute(nickname=to, message='third post message')

class TestSocialNetwork_Mentions(unittest.TestCase):

    def setUp(self):
        self.timelineRepository = TimelineRepository()
        self.postMessage = PostMessage(self.timelineRepository)
        self.mentionsSomeone = MentionsSomeone(self.timelineRepository)

    def test_can_metions_in_message_personal_timeline(self):
        self.postMessage.execute(nickname='arodriguez', message='hello @rafa')
        post = self.timelineRepository.findPost(nickname='arodriguez',message='hello @rafa')
        self.mentionsSomeone.execute('arodriguez',post)
        was_it_metioned = self.timelineRepository.hasMentionedTo(nickname='rafa', post=post)
        self.assertEqual(was_it_metioned, True)

class TestSocialNetwork_Links(unittest.TestCase):

    def setUp(self):
        self.timelineRepository = TimelineRepository()
        self.postMessage = PostMessage(self.timelineRepository)
        self.linkSomething = LinkSomething(self.timelineRepository)

    def test_can_metions_in_message_personal_timeline(self):
        self.postMessage.execute(nickname='arodriguez', message='Visit my https://website.co')
        post = self.timelineRepository.findPost(nickname='arodriguez',message='Visit my https://website.co')
        self.linkSomething.execute('arodriguez', post)
        was_it_metioned = self.timelineRepository.hasLink(link='https://website.co', post=post)
        self.assertEqual(was_it_metioned, True)

if '__main__' == __name__:
    unittest.main()
