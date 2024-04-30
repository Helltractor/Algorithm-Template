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
        b = LII()
        ba = [(y, x) for x, y in zip(a, b)]
        ba.sort()
        ret = []
        tmp = 0
        for y, x in ba:
            tmp += max(0, y - x)
            ret.append(tmp)
        h = []
        sm = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            y, x = ba[i]
            if len(h) == k:
                ans = max(ans, ret[i] - sm)
            sm += x
            heappush(h, -x)
            if len(h) > k:
                sm += heappop(h)
        print(ans)
    return 
   
main()