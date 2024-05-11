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
    from heapq import heapify, heappop, heappush
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, comb
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

def main():
    mod = 10 ** 9 + 7
    m = 3 * 10 ** 5 + 1
    l = 3 * pow(10, 5) + 5
    fact = [1] * (l + 1)
    for i in range(1, l + 1):
        fact[i] = i * fact[i - 1] % mod
    inv = [1] * (l + 1)
    inv[l] = pow(fact[l], mod - 2, mod)
    for i in range(l - 1, -1, -1):
        inv[i] = (i + 1) * inv[i + 1] % mod
    def comb(n, r):
        return fact[n] * inv[r] % mod * inv[n - r] % mod if n >= r >= 0 else 0
    f = [1] * m
    for i in range(1, m):
        f[i] = f[i - 2] * i
    f += [1]
    for _ in range(II()):
        n, k = MII()
        a = [LII() for i in range(k)]
        cnt = n
        mod = 10 ** 9 + 7
        for x, y in a:
            cnt -= 2 - int(x == y)
        ans = 0
        for i in range(cnt // 2 + 1):
            ans = (ans + comb(cnt, 2 * i) * max(1, f(2 * i - 1)) * pow(2, i, mod)) % mod
        print(ans)
    return

main()