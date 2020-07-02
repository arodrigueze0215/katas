import unittest
from circular_prime import CircularPrime

class TestCircularPrime(unittest.TestCase):

    def setUp(self):
        self.circularPrime = CircularPrime()


    def test_is_prime(self):
        is_prime = self.circularPrime.is_prime(19)
        self.assertEqual(is_prime, True)

    def test_isnt_prime(self):
        is_prime = self.circularPrime.is_prime(9)
        self.assertEqual(is_prime, False)

    def test_circle_number(self):
        number_circle = self.circularPrime.number_circle('971')
        self.assertEqual(number_circle, '719')
        number_circle = self.circularPrime.number_circle('719')
        self.assertEqual(number_circle, '197')

    def test_is_circular_prime_971(self):
        circular_prime_result = self.circularPrime.circular_prime_calc('971')
        self.assertEqual(circular_prime_result, True)

    def test_is_circular_prime_20(self):
        circular_prime_result = self.circularPrime.circular_prime_calc('20')
        self.assertEqual(circular_prime_result, False)

    def test_how_many_circular_prime_are_in_1(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(1)
        self.assertEqual(circular_prime_result, 0)
    def test_how_many_circular_prime_are_in_10(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(10)
        self.assertEqual(circular_prime_result, 4)

    def test_how_many_circular_prime_are_in_100(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(100)
        self.assertEqual(circular_prime_result, 13)

    def test_how_many_circular_prime_are_in_1000(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(1000)
        self.assertEqual(circular_prime_result, 25)

    def test_how_many_circular_prime_are_in_10000(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(10000)
        self.assertEqual(circular_prime_result, 33)

    def test_how_many_circular_prime_are_in_100000(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(100000)
        self.assertEqual(circular_prime_result, 43)

    def test_how_many_circular_prime_are_in_1000000(self):
        circular_prime_result = self.circularPrime.how_many_circular_prime(1000000)
        self.assertEqual(circular_prime_result, 55)
    """
    """

if '__main__' == __name__:
    unittest.main()
