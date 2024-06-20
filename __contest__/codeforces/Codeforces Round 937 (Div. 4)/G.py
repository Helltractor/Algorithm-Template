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


def G():
    for _ in range(II()):
        n = II()
        a = [LI() for _ in range(n)]
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
                    g[i].append(j)
        visit = [[False] * n for _ in range(1 << n)]
        ans = [10 ** 18] * (1 << n)
        q = deque()
        for i in range(n):
            ans[1 << i] = 1
            q.append((1 << i, i))
            visit[1 << i][i] = True
        while q:
            mask, u = q.popleft()
            for v in g[u]:
                if mask & (1 << v) == 0 and not visit[mask | (1 << v)][v]:
                    visit[mask | (1 << v)][v] = True
                    ans[mask | (1 << v)] = min(ans[mask | (1 << v)], ans[mask] + 1)
                    q.append((mask | (1 << v), v))
        res = 10 ** 18
        for i in range(1 << n):
            if ans[i] <= n:
                res = min(res, n - ans[i])
        print(res)
    return


def main():
    G()
    return


if __name__ == '__main__':
    main()
