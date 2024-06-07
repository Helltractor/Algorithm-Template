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
    from bisect import bisect_left, bisect_right, bisect
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
        n, q = MII()
        a = LII()
        pre = [RD] * (n + 1)
        cnt = defaultdict(list)
        for i, x in enumerate(a, 1):
            pre[i] = pre[i - 1] ^ x
        for i in range(n + 1):
            cnt[pre[i]].append(i)

        # x y x y
        for _ in range(q):
            l, r = MII()
            if pre[r] == pre[l - 1]:
                print("Yes")
            else:
                p = cnt[pre[r]][bisect_left(cnt[pre[r]], l - 1)]
                if p == r:
                    print("No")
                else:
                    p = bisect_left(cnt[pre[l - 1]], p)
                    if p == len(cnt[pre[l - 1]]) or cnt[pre[l - 1]][p] >= r:
                        print("No")
                    else:
                        print("Yes")
        print()
    return 
   
main()