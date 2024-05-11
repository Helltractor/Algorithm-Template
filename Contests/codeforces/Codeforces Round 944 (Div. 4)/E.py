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
    inf = 10 ** 18
    Y = "Yes"
    N = "No"
 
def cf_E():
    for _ in range(II()):
        n, k, q = MII()
        # a = LII()
        # b = LII()
        # v = sum(y / x for x, y in zip(a, b)) / k
        # ans = []
        # for _ in range(q):
        #     x = II()
        #     ans.append(round(x * v))
        # print(*ans)
        a = [0] + LII()
        a.append(2 * a[-1])
        b = [0] + LII()
        b.append(2 * b[-1])
        ans = []
        for _ in range(q):
            x = II()
            i = bisect_left(a, x)
            if a[i] == x:
                ans.append(b[i])
            else:
                i -= 1
                # print(a[i], a[i + 1], b[i], b[i + 1])
                tmp = (b[i + 1] - b[i]) * (x - a[i]) // (a[i + 1] - a[i])
                ans.append(floor(tmp + b[i]))
        print(*ans)
    return 
 
def main():
    cf_E()
    return 
 
if __name__ == '__main__':
    main()