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


def cf_264C():
    n, q = MII()
    v = LII()
    c = LII()
    ans = []
    for _ in range(q):
        a, b = MII()
        f = [-10 ** 18] * (n + 1)
        mx1 = mx2 = maxC = 0
        for i in range(n):
            x, y = v[i], c[i]
            mx = mx1 if y != maxC else mx2
            f[y] = max(f[y] + max(0, a * x), max(mx, 0) + x * b)
            if f[y] > mx1:
                if y != maxC:
                    maxC = y
                    mx2 = mx1
                mx1 = f[y]
            elif y != maxC and f[y] > mx2:
                mx2 = f[y]
        ans.append(mx1)
    print("\n".join(map(str, ans)))
    return


def main():
    cf_264C()
    return


if __name__ == '__main__':
    main()
