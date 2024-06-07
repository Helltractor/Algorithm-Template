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

# 4
# 1 0
# 2 1
# 1 2
# 0 2
# 4 5 5
# 5 4 1
# 1 2
# 2 1 5 4
# 5 2 3 1
# 3 1
# 4 3 3 4 1
# 5 5 4 5 2


def cf_C():
    for _ in range(II()):
        n, m = MII()
        a = LII()
        b = LII()
        s = n + m + 1
        c = []
        d = []
        for i, (x, y) in enumerate(zip(a, b)):
            if x > y:
                c.append(i)
            else:
                d.append(i)
        cur = c + d[::-1]
        pre_a = [0] * (s + 1)
        pre_b = [0] * (s + 1)
        for i in range(s):
            pre_a[i + 1] = pre_a[i] + a[cur[i]]
            pre_b[i + 1] = pre_b[i] + b[cur[i]]
        ans = [0] * s
        for i, x in enumerate(cur):
            if i < n:
                ans[x] = pre_a[n + 1] - a[x] + pre_b[s] - pre_b[n + 1]
            elif i == n:
                ans[x] = pre_a[n] + pre_b[s] - pre_b[n + 1]
            else:
                ans[x] = pre_a[n] + pre_b[s] - pre_b[n] - b[x]
        
        print(*ans)
    return


def main():
    cf_C()
    return


if __name__ == '__main__':
    main()
