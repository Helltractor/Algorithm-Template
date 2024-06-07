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

def test():
    for a in [*open(0)][1:]:
        n, x = map(int, a.split())
        if n % x:
            print(-1)
            continue
        y = n // x
        i = 2
        p = []
        while y > 1:
            if y % i == 0:
                p += i
                y //= i
            else:
                i += 1
        ans = list(range(1, n + 1))
        ans[0], ans[-1] = x, 1
        for d in p:
            ans[x] = ans[x * d]
            x *= d
        print(*ans)
    return

def cf_1758C():
    for _ in range(II()):
        n, x = MII()
        ans = list(range(1, n + 1))
        if n == x:
            ans[0], ans[x - 1] = ans[x - 1], ans[0]
            print(*ans)
        elif n % x == 0:
            ans[0], ans[x - 1], ans[-1] = x, n, 1
            x -= 1
            for i in range(1, n - 1):
                if ans[i] % (x + 1) == ans[x] % (i + 1) == 0:
                    ans[i], ans[x] = ans[x], ans[i]
                    x = i
            print(*ans)
        else:
            print(-1)
    return


def main():
    # test()
    cf_1758C()
    return


if __name__ == '__main__':
    main()
