import unittest
from Application.Users.commands.register_user import RegisterUser
from Application.Users.commands.follow_user import FollowUser
from Application.Users.queries.is_following import IsFollowing
from Infrastructure.User.repository import Repository

class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.repository = Repository()
        self.registerUser = RegisterUser(self.repository)
        self.followUser = FollowUser(self.repository)
    """
        Un usuario puede registrarse con un nombre de usuario. Por ejemplo: “@veritran"
        Si otra persona se ha registrado usando ese mismo nombre de usuario se produce un error.
    """
    def test_register_user(self):
        self.registerUser.execute('arodriguez')
        with self.assertRaises(Exception):
            self.registerUser.execute('arodriguez')


    """
    Un usuario puede seguir a otros usuarios.
    Para hacerlo basta con conocer el nickname del usuario al que se quiere seguir.
    Cualquiera debe poder consultar a quién sigue un determinado usuario conociendo su nickname.
    """
    def test_follow_user(self):
        isFollowing = IsFollowing(self.repository)
        self.registerUser.execute('jAbril')
        self.registerUser.execute('arodriguez')
        self.followUser.execute('arodriguez','jAbril')
        self.assertEqual(isFollowing.execute('arodriguez','jAbril'), True)

    def test_follow_myself(self):
        self.registerUser.execute('arodriguez')
        with self.assertRaises(Exception):
            self.followUser.execute('arodriguez','arodriguez')

    def test_follow_nonexist_user(self):
        self.registerUser.execute('arodriguez')
        with self.assertRaises(Exception):
            self.followUser.execute('arodriguez','dCasta')

    def test_follow_already_user_following(self):
        self.registerUser.execute('jAbril')
        self.registerUser.execute('arodriguez')
        self.followUser.execute('arodriguez','jAbril')
        with self.assertRaises(Exception):
            self.followUser.execute('arodriguez','jAbril')



if __name__ == '__main__':
    unittest.main()
