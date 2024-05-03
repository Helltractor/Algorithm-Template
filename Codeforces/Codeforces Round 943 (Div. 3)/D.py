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
        n, k, pb, ps = MII()
        pb -= 1
        ps -= 1
        p = LII()
        a = LII()
        b = 0
        s = 0
        bb = 0
        ss = 0
        for i in range(n):
            b = max(b, bb + a[pb] * max(0, k - i))
            if k > i:
                bb += a[pb]
            pb = p[pb] - 1
            s = max(s, ss + a[ps] * max(0, k - i))
            if k > i:
                ss += a[ps]
            ps = p[ps] - 1
        # print(b, s)
        if b < s:
            print("Sasha")
        elif b == s:
            print("Draw")
        else:
            print("Bodya")




    return 
   
main()