# _*_ coding: utf-8 _*_
# @File : primes_factor.py
# @Time : 2023/11/30 19:19
# @Author : Helltractor
from collections import Counter

from typing import List


class PrimesFactor:
    """ 统计每个数的质因子的个数"""

    # count = [0] * n
    # for i in range(2, n):
    #     if count[i] == 0:
    #         for j in range(i, n, i):
    #             count[j] += 1

    def count_primes_factor(n: int) -> int:
        cnt = [0] * n
        for i in range(2, n):
            if cnt[i] == 0:
                for j in range(i, n, i):
                    cnt[j] += 1
        return cnt

    """统计每个数的质因子个数"""

    # fac = [[] for _ in range(n)]
    # for i in range(2, n):
    #     if not fac[i]:
    #         for j in range(i, n, i):
    #             fac[j].append(i)

    def primes_factor(n: int) -> List[List[int]]:
        fac = [[] for _ in range(n)]
        for i in range(2, n):
            if not fac[i]:
                for j in range(i, n, i):
                    fac[j].append(i)
        return fac
    
    """
        统计一个数的质因子个数
        a = p1 ^ e1 * p2 ^ e2 * p3 ^ e3
    """
    
    def prime_factor(n: int) -> Counter:
        count = Counter()
        d = 2
        while d * d <= n:
            while n % d == 0:
                count[d] += 1
                n //= d
            d += 1
        if n > 1:
            count[n] += 1
        return count