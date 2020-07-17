class ViewTimeline(object):

    def __init__(self, timelineRepository):
        self.timelineRepository = timelineRepository

    def execute(self, **args):
        timeline = self.timelineRepository.findTimelineByNickname(args.get('nickname'))
        return timeline
