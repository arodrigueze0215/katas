import unittest
from Application.Users.user import User
from Application.Users.listUser import List

class TestTwitter(unittest.TestCase):
    def test_registerUser(self):
        userT = User('arodriguez')
        usersList = List()
        usersList.add(userT)
        with self.assertRaises(Exception):
            usersList.add(userT)


if __name__ == '__main__':
    unittest.main()