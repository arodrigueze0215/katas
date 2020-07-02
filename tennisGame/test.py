import unittest
from game import Game
from player import Player
class TestTennisGame(unittest.TestCase):
    """Kata for TestTennisGame. for more information please read the README.md file"""

    def setUp(self):
        self.playerOne = Player('Andres')
        self.playerTwo = Player('Rafa')


    """
     Scores from zero to three points are described as “love”, “fifteen”, “thirty”, and “forty” respectively.
    """
    def test_score_point(self):
        game = Game()
        game.start(self.playerOne, self.playerTwo)
        score = game.score_point(self.playerOne)
        self.assertEqual(score, 'love')
        score = game.score_point(self.playerOne, 1)
        self.assertEqual(score, 'fifteen')

    """
    If at least three points have been scored by each side and a player has one more point than his opponent,
    the score of the game is “advantage” for the player in the lead.
    """
    def test_game_advantage(self):
        game = Game()
        game.start(self.playerOne, self.playerTwo)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 1)
        game.score_point(self.playerTwo, 0)
        game.score_point(self.playerTwo, 1)
        score = game.score_result()
        self.assertEqual(score[self.playerOne.name],'advantage')

    """
        If at least three points have been scored by each player, and the scores are equal, the score is “deuce”.
    """
    def test_game_deuce(self):
        game = Game()
        game.start(self.playerOne, self.playerTwo)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 1)
        game.score_point(self.playerTwo, 1)
        game.score_point(self.playerTwo, 1)
        score = game.score_result()
        self.assertEqual(score[self.playerOne.name],'deuce')
        self.assertEqual(score[self.playerTwo.name],'deuce')

    """
        A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
    """
    def test_game_won(self):
        game = Game()
        game.start(self.playerOne, self.playerTwo)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 1)
        game.score_point(self.playerTwo, 0)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 0)
        score = game.score_result()
        self.assertEqual(score[self.playerOne.name],'winner')
    """
        A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
    """
    def test_game_won2(self):
        game = Game()
        game.start(self.playerOne, self.playerTwo)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 0)
        game.score_point(self.playerTwo, 0)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 0)
        game.score_point(self.playerOne, 1)
        game.score_point(self.playerTwo, 0)
        score = game.score_result()
        self.assertEqual(score[self.playerOne.name],'winner')




if __name__ == '__main__':
    unittest.main()
