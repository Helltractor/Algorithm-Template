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


def B():
    for _ in range(II()):
        n, m = MII()
        a = [LII() for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cnt = 0
                s = 0
                tmp = 0
                if i - 1 >= 0:
                    cnt += a[i - 1][j] < a[i][j]
                    s += 1
                    tmp = max(tmp, a[i - 1][j])
                if i + 1 < n:
                    cnt += a[i + 1][j] < a[i][j]
                    s += 1
                    tmp = max(tmp, a[i + 1][j])
                if j - 1 >= 0:
                    cnt += a[i][j - 1] < a[i][j]
                    s += 1
                    tmp = max(tmp, a[i][j - 1])
                if j + 1 < m:
                    cnt += a[i][j + 1] < a[i][j]
                    s += 1
                    tmp = max(tmp, a[i][j + 1])
                if cnt == s != 0:
                    a[i][j] = tmp
        for i in a:
            print(*i)
    return


def main():
    B()
    return


if __name__ == '__main__':
    main()
