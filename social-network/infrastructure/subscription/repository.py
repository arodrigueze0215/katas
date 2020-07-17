from domain.subscription.subscription import Subscription
class Repository(object):

    def __init__(self):
        self.subscription_list = {}

    def listAllSubscriptions(self):
        return self.subscription_list

    def save(self, user_timeline, subscription):
        self.subscription_list[user_timeline] = subscription
