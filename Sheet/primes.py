# _*_ coding: utf-8 _*_
# @File : primes.py
# @Time : 2023/11/30 19:19
# @Author : Helltractor
from typing import List


# fool idea
def fool_Primes(n):
    primes = []
    for i in range(2, n):
        if all(i % j != 0 for j in range(2, i)):
            primes.append(i)
    return primes


# 枚举
def Primes_enumeration(n: int) -> int:
    def isPrime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True if n > 1 else False

    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes


# 枚举优化
def Primes_enumeration_plus(n: int) -> int:
    def isPrime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True if n > 1 else False

    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes


# 埃氏筛
"""
    primes = []
    is_prime = [True] * n
    # is_prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i ** 2, n, i):
                is_prime[j] = False
    primes.extend([n, n])   # 防止下标越界
"""


def Primes_Ealich(n: int) -> int:
    primes = []
    is_prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i ** 2, n, i):
                is_prime[j] = False
    return primes


# 线性筛
"""
    primes = []
    is_prime = [True] * n
    # is_prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p >= n: break
            is_prime[i * p] = False
            if i % p == 0: break
    primes.extend([n, n])   # 防止下标越界
"""


def Primes_linear(n: int) -> int:
    primes = []
    is_prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p >= n:  break
            is_prime[i * p] = False
            if i % p == 0:  break
    return primes


# 统计每个数的质因子的个数
"""
    count = [0] * n
    for i in range(2, n):
        if count[i] == 0:
            for j in range(i, n, i):
                count[j] += 1
"""


def count_Prime_factor(n: int) -> int:
    cnt = [0] * n
    for i in range(2, n):
        if cnt[i] == 0:
            for j in range(i, n, i):
                cnt[j] += 1
    return cnt


# 统计每个数的质因子
"""
    fac = [[] for _ in range(n)]
    for i in range(2, n):
        if not fac[i]:
            for j in range(i, n, i):
                fac[j].append(i)
"""


def Prime_factor(n: int) -> List[List[int]]:
    fac = [[] for _ in range(n)]
    for i in range(2, n):
        if not fac[i]:
            for j in range(i, n, i):
                fac[j].append(i)
    return fac