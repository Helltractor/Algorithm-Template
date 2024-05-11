import heapq

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


def main():
    for _ in range(II()):
        n, k = MII()
        a = LII()
        d = {i: v for i, v in enumerate(a)}
        def dfs(i, d):
            if i == k:
                return sum(d.values())
            ret = 10 ** 18

            for j in range(n):
                if j == 0:
                    if d[j] == d[j + 1]:
                        continue
                    tmp = d[j + 1]
                    d[j + 1] = d[j]
                    ret = min(ret, dfs(i + 1, d))
                    d[j + 1] = tmp
                elif j == n - 1:
                    if d[j] == d[j - 1]:
                        continue
                    tmp = d[j - 1]
                    d[j - 1] = d[j]
                    ret = min(ret, dfs(i + 1, d))
                    d[j - 1] = tmp
                else:
                    if d[j] != d[j - 1]:
                        tmp = d[j - 1]
                        d[j - 1] = d[j]
                        ret = min(ret, dfs(i + 1, d))
                        d[j - 1] = tmp
                    if d[j] != d[j + 1]:
                        tmp = d[j + 1]
                        d[j + 1] = d[j]
                        ret = min(ret, dfs(i + 1, d))
                        d[j + 1] = tmp
            return ret

        if n == 1:
            print(a[0])
        else:
            print(dfs(0, d))
    return


main()