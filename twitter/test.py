import unittest
from Application.Users.registerUser import RegisterUser
from Application.Users.followUser import FollowUser

class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.registerUser = RegisterUser()
    """
        Un usuario puede registrarse con un nombre de usuario. Por ejemplo: “@veritran"
        Si otra persona se ha registrado usando ese mismo nombre de usuario se produce un error.
    """
    def test_registerUser(self):
        self.registerUser.register('arodriguez')
        with self.assertRaises(Exception):
            self.registerUser.register('arodriguez')


    """
    Un usuario puede seguir a otros usuarios.
    Para hacerlo basta con conocer el nickname del usuario al que se quiere seguir.
    Cualquiera debe poder consultar a quién sigue un determinado usuario conociendo su nickname.
    """
    def test_followUser(self):
        self.registerUser.register('jAbril')
        self.registerUser.register('jLopez')
        userJAbril = self.registerUser.getUserRegistered('jAbril')
        userJLopez = self.registerUser.getUserRegistered('jLopez')
        followUser = FollowUser(userJAbril)
        followUser.follow(userJLopez)
        self.assertEqual(followUser.isFollowing(userJLopez), True)




if __name__ == '__main__':
    unittest.main()
