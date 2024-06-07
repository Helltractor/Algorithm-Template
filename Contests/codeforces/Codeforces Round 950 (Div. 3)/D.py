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


def D():
    for _ in range(II()):
        n = II()
        a = LII()
        b = []
        for i in range(n - 1):
            b.append(gcd(a[i], a[i + 1]))
        s = sum(b[i] > b[i + 1] for i in range(len(b) - 1))
        flag = False
        if s - int(b[0] > b[1]) == 0:
            flag = True
        if s - int(b[-2] > b[-1]) == 0:
            flag = True
        for i in range(1, n - 1):
            tmp = s
            tmp -= int(b[i - 1] > b[i])
            g = gcd(a[i - 1], a[i + 1])
            if i - 1 > 0:
                tmp -= int(b[i - 2] > b[i - 1])
                tmp += int(b[i - 2] > g)
            if i + 1 < n - 1:
                tmp -= int(b[i] > b[i + 1])
                tmp += int(g > b[i + 1])
            if tmp == 0:
                flag = True
        print(Y if flag else N)

    return


def main():
    D()
    return


if __name__ == '__main__':
    main()
