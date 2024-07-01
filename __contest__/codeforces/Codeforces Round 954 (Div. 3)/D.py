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
        s = I()
        ans = 10 ** 18
        if n == 2:
            print(int(s))
        elif s[0] == "0" or s[-1] == "0":
            print(0)
        else:
            a = []
            cnt = 0
            for i, x in enumerate(map(int, s)):
                if x == 0:
                    cnt += 1
                a.append(x)
            if cnt >= 1 and n > 3:
                ans = 0
            else:
                for i in range(n - 1):
                    tmp = a[i] * 10 + a[i + 1]
                    for j in range(0, i):
                        if tmp == 1:
                            tmp *= a[j]
                        else:
                            if a[j] == 1:
                                tmp *= a[j]
                            else:
                                tmp += a[j]
                            
                    for j in range(i + 2, n):
                        if tmp == 1:
                            tmp *= a[j]
                        else:
                            if a[j] == 1:
                                tmp *= a[j]
                            else:
                                tmp += a[j]
                    ans = min(ans, tmp)
            print(ans)
    return


def main():
    D()
    return


if __name__ == '__main__':
    main()
