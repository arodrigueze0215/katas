class Game(object):
    """docstring for Game."""
    def __init__(self):
        self.scores_game = {}
        self.score_total = {}

    def score_point(self, player, point=0):
        if point == 1:
            acumulate = self.scores_game[player.name]
            acumulate += point
            self.scores_game[player.name] = acumulate
        return self._return_value(self.scores_game[player.name])

    def start(self, playerOne, playerTwo):
        self.scores_game[playerOne.name] = 0
        self.scores_game[playerTwo.name] = 0

    def score_result(self):
        score_total = max(self.scores_game.values()) - min(self.scores_game.values())
        keys = [key for key in self.scores_game.keys() if self.scores_game[key] == max(self.scores_game.values())]        
        if len(keys) > 1:
            return {
                keys[0]: 'deuce',
                keys[1]: 'deuce'
            }
        elif score_total >= 2:
            return {
                keys[0]: 'winner'
            }
        else:
            return {
                keys[0]: 'advantage'
            }

    def _return_value(self, point=0):
        values = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }
        return values.get(point, 'invalid point')
