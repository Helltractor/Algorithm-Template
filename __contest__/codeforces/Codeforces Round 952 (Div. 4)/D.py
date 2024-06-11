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


def D():
    for _ in range(II()):
        n, m = MII()
        low, high = n - 1, 0
        left, right = m - 1, 0
        a = [I() for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # print(a, i, j, n, m)
                if a[i][j] == '#':
                    low = min(low, i)
                    high = max(high, i)
                    left = min(left, j)
                    right = max(right, j)
        x = (low + high) // 2
        y = (left + right) // 2
        print(x + 1, y + 1)
    return


def main():
    D()
    return


if __name__ == '__main__':
    main()
