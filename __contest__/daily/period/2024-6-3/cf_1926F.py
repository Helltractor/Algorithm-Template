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


def cf_1926F():
    for _ in range(II()):
        grid = [I() for _ in range(7)]
        d = dict()
        cnt = 0
        for x in range(1, 6):
            for y in range(1, 6):
                if grid[x][y] == grid[x + 1][y + 1] == grid[x - 1][y - 1] == grid[x + 1][y - 1] == grid[x - 1][y + 1] == 'B':
                    d[(x, y)] = cnt
                    cnt += 1
        
        bit_to_mask = defaultdict(list)
        for x in range(1, 6):
            for y in range(1, 6):
                mask = 0
                for dx, dy in (x, y), (x + 1, y + 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y - 1):
                    if (dx, dy) in d:
                        mask |= 1 << d[(dx, dy)]
                for i in range(cnt):
                    if mask >> i & 1:
                        bit_to_mask[1 << i].append(mask)
        
        ans = 1e18
        def dfs(mask, cnt):
            if mask == 0:
                nonlocal ans
                ans = min(ans, cnt)
                return
            if cnt > 8:
                return
            lb = mask & -mask
            for m in bit_to_mask[lb]:
                dfs(mask & ~m, cnt + 1)
        dfs((1 << cnt) - 1, 0)
        print(ans)
        
    return


def main():
    cf_1926F()
    return


if __name__ == '__main__':
    main()
