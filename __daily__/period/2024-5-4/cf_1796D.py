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


def cf_1796D():
    for _ in range(II()):
        n, k, x = MII()
        a = LII()
        if x < 0:
            x = -x
            k = n - k
        ans = -10 ** 18
        pre = pre_ = min_pre = 0
        for i in range(n):
            pre += a[i] - x
            if i >= k:
                ans = max(ans, pre - min_pre + 2 * x * k)
                pre_ += a[i - k] - x
                min_pre = min(min_pre, pre_)
                
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + a[i] + x
        q = deque([0])
        for i in range(1, n + 1):
            if q[0] < i - k:
                q.popleft()
            while q and s[q[-1]] >= s[i]:
                q.pop()
            q.append(i)
            ans = max(ans, s[i] - s[q[0]])
        print(ans)
        
    return


def main():
    cf_1796D()
    return


if __name__ == '__main__':
    main()
