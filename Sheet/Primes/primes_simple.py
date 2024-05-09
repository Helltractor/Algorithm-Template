# _*_ coding: utf-8 _*_
# @File : primes_simple.py
# @Time : 2024/5/9 17:06
# @Author : Helltractor
import time
import unittest


class Primes:

    def fool_primes(n):
        primes = []
        for i in range(2, n):
            if all(i % j != 0 for j in range(2, i)):
                primes.append(i)
        return primes

    def primes_enumeration(n: int) -> int:
        """枚举"""
        def is_prime(n):
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True if n > 1 else False

        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes

    def primes_enumeration_plus(n: int) -> int:
        """枚举优化"""
        def is_prime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True if n > 1 else False

        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes

class TestGeneral(unittest.TestCase):
    def test_primes_enumeration(self):
        start_time = time.time()
        Primes.primes_enumeration(pow(2, 16))
        end_time = time.time()
        print('primes_enumeration:', end_time - start_time)
        return

    def test_primes_enumeration_plus(self):
        start_time = time.time()
        Primes.primes_enumeration_plus(pow(2, 16))
        end_time = time.time()
        print('primes_enumeration_plus:', end_time - start_time)
        return

if __name__ == '__main__':
    TestGeneral().main()