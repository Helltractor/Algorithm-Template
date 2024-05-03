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

def check(x, a, b):
    if x > len(b):
        return False
    cnt = 0
    j = 0
    # print(x, a[:x])
    for i in range(x):
        while j < len(b) and a[i] != b[j]:
            j += 1
        if j >= len(b):
            break
        if a[i] == b[j]:
            cnt += 1
            j += 1
            # print(i, j)
    # print(cnt, x)
    return cnt == x
def main():
    for _ in range(II()):
        n, m = MII()
        a = I()
        b = I()
        l = 0
        r = n
        while l <= r:
            mid = (l + r) >> 1
            # print(l, r, mid)
            if check(mid, a, b):
                l = mid + 1
            else:
                r = mid - 1
        print(r)
    return 
   
main()