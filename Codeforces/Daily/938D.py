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
    n, m = MII()
    grid = [[] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = MII()
        grid[x].append((y, w * 2))
        grid[y].append((x, w * 2))
    a = LII()
    for i, x in enumerate(a, 1):
        grid[0].append((i, x))
        grid[i].append((0, x))
    dis = [10 ** 18] * (n + 1)
    dis[0] = 0
    h = [(0, 0)]
    while h:
        cost, x = heappop(h)
        if cost > dis[x]:
            continue
        for y, w in grid[x]:
            if dis[y] > cost + w:
                dis[y] = cost + w
                heappush(h, (dis[y], y))
    print("\n".join(map(str, dis[1:])))
    return 
   
main()