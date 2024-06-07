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

def cf_650D():
    n, q = MII()
    a = LII()
    d = defaultdict(list)
    for i in range(q):
        a_idx, b = MII()
        d[a_idx - 1].append((b, i))
    ans = [0] * q
    pre = [0] * n
    suf = [0] * n
    g = []
    for i, v in enumerate(a):
        for val, idx in d[i]:
            ans[idx] = bisect_left(g, val) + 1
        p = bisect_left(g, v)
        if p < len(g):
            g[p] = v
        else:
            g.append(v)
        pre[i] = p + 1
    g = []
    for i in range(n - 1, -1, -1):
        for val, idx in d[i]:
            ans[idx] += bisect_left(g, -val)
        v = -a[i]
        p = bisect_left(g, v)
        if p < len(g):
            g[p] = v
        else:
            g.append(v)
        suf[i] = p + 1
    lis = len(g)
    cnt = [0] * (n + 1)
    for i, p in enumerate(pre):
        if p + suf[i] - 1 == len(g):
            cnt[p] += 1
    for i, p in enumerate(pre):
        k = lis
        if p + suf[i] - 1 == len(g) and cnt[p] == 1:
            k -= 1
        for val, idx in d[i]:
            ans[idx] = max(ans[idx], k)
    print(*ans, sep='\n')
    return


def main():
    cf_650D()
    return


if __name__ == '__main__':
    main()
