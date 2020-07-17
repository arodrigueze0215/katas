from domain.subscription.subscription import Subscription
class Subscribe(object):

    def __init__(self, timelineRepository, subscriptionRepository):
        self.timelineRepository = timelineRepository
        self.subscriptionRepository = subscriptionRepository

    def execute(self, nickname):
        timeline = self.timelineRepository.findTimelineByNickname(nickname)
        subscription = Subscription(nickname, timeline)
        self.subscriptionRepository.save(nickname, subscription)
