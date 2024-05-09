import time
import unittest

from Sheet.Primes.primes_linear import Linear
from Sheet.Primes.primes_simple import Primes
from Sheet.Primes.primes_ealich import Ealich


class MyTestCase(unittest.TestCase):
    n = pow(2, 16)

    def test_primes_linear(self):
        start_time = time.time()
        Linear.primes_linear(self.n)
        end_time = time.time()
        print('primes_linear:', end_time - start_time)
        return

    def test_primes_ealich(self):
        start_time = time.time()
        Ealich.primes_ealich(self.n)
        end_time = time.time()
        print('primes_ealich:', end_time - start_time)
        return

    def test_primes_enumeration(self):
        start_time = time.time()
        Primes.primes_enumeration(self.n)
        end_time = time.time()
        print('primes_enumeration:', end_time - start_time)
        return

    def test_primes_enumeration_plus(self):
        start_time = time.time()
        Primes.primes_enumeration_plus(self.n)
        end_time = time.time()
        print('primes_enumeration_plus:', end_time - start_time)
        return


if __name__ == '__main__':
    unittest.main()