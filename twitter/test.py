import unittest
from Application.Users.commands.register_user import RegisterUser
from Application.Users.commands.follow_user import FollowUser
from Application.Users.queries.is_following import IsFollowing
from Domain.User.repository import Repository

class TestTwitter(unittest.TestCase):
    """
        Un usuario puede registrarse con un nombre de usuario. Por ejemplo: “@veritran"
        Si otra persona se ha registrado usando ese mismo nombre de usuario se produce un error.
    """
    def test_registerUser(self):
        repository = Repository()
        registerUser = RegisterUser(repository)
        registerUser.execute('arodriguez')
        with self.assertRaises(Exception):
            registerUser.execute('arodriguez')


    """
    Un usuario puede seguir a otros usuarios.
    Para hacerlo basta con conocer el nickname del usuario al que se quiere seguir.
    Cualquiera debe poder consultar a quién sigue un determinado usuario conociendo su nickname.
    """
    def test_followUser(self):
        repository = Repository()
        registerUser = RegisterUser(repository)
        followUser = FollowUser(repository)
        isFollowing = IsFollowing(repository)
        registerUser.execute('jAbril')
        registerUser.execute('arodriguez')
        followUser.execute('arodriguez','jAbril')

        self.assertEqual(isFollowing.execute('arodriguez','jAbril'), True)




if __name__ == '__main__':
    unittest.main()
