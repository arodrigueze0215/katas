class CircularPrime(object):
    def __init__(self):
        super(CircularPrime, self).__init__()

    def is_prime(self, number):
        if number == 2:
             return True
        if (number < 2) or not (number % 2):
            return False

        for i in range(3, int(number**0.5) + 1, 2):
            if (number % i) == 0:
               return False
        return True

    def number_circle(self, number):
        numL = list(str(number))
        firstN = numL.pop(0)
        numL.append(firstN)
        return ''.join(numL)

    def circular_prime_calc(self, number):
        num_circle = number
        for i in range(0, len(str(number))):
            if self.is_prime(int(num_circle)) == False:
                return False
            num_circle = self.number_circle(num_circle)
        return True

    def how_many_circular_prime(self, number):
        circular_prime_count = 0
        for i in range(2, int(number)):
            c_prime_calc = self.circular_prime_calc(i)
            if c_prime_calc == True:
                circular_prime_count += 1

        return circular_prime_count
