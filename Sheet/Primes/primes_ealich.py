# _*_ coding: utf-8 _*_
# @File : primes_ealich.py
# @Time : 2024/5/9 17:17
# @Author : Helltractor

class Ealich:
    """埃氏筛"""

    # primes = []
    # is_prime = [True] * n
    # # is_prime = [False] * 2 + [True] * (n - 2)
    # for i in range(2, n):
    #     if is_prime[i]:
    #         primes.append(i)
    #         for j in range(i ** 2, n, i):
    #             is_prime[j] = False
    # primes.extend([n, n])   # 防止下标越界

    def primes_ealich(n: int) -> int:
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
                for j in range(i ** 2, n, i):
                    is_prime[j] = False
        return primes