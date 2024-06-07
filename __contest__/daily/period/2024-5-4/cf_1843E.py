ImportType = 1
InputType = 1
ConstType = 1
if ImportType:
    import os, sys, random, threading
    from random import randint, choice, shuffle
    from copy import deepcopy
    from io import BytesIO, IOBase
    from types import GeneratorType
    from functools import lru_cache, reduce
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush, heappushpop
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, comb, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    from decimal import Decimal, getcontext
    from sys import stdin, stdout, setrecursionlimit

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    I = lambda: input()
    II = lambda: int(input())
    MII = lambda: map(int, input().split())
    LI = lambda: list(input().split())
    LII = lambda: list(map(int, input().split()))
    GMI = lambda: map(lambda x: int(x) - 1, input().split())
    LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353
    Y = "Yes"
    N = "No"


# 时间复杂度： O(m + q + (q + m)logq) ≈ O((q + m)logq)
def check(i, a, b, n):
    pre = [0] * (n + 1)
    for j in b[:i]:
        pre[j] = 1
    for j in range(n):
        pre[j + 1] += pre[j]
    for l, r in a:
        if (pre[r + 1] - pre[l]) * 2 > r - l + 1:
            return True
    return False

def cf_1843E():
    for _ in range(II()):
        n, m = MII()
        a = [LGMI() for _ in range(m)]
        q = II()
        b = [II() for _ in range(q)]
        l = 1
        r = q
        while l <= r:
            mid = l + r >> 1
            if check(mid, a, b, n):
                r = mid - 1
            else:
                l = mid + 1
        print(l if l <= q else -1)
    
    return


def main():
    cf_1843E()
    return


if __name__ == '__main__':
    main()
