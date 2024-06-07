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
        n, k = MII()
        s = I()
        x = 0
        for i in range(n - 1, -1, -1):
            if s[i] == s[-1]:
                x += 1
            else:
                break
        
        def check():
            for i in range(k):
                if s[i] != s[0]:
                    return False
            for i in range(n - k):
                if s[i] == s[i + k]:
                    return False
            return True
        
        def operation(p):
            nonlocal s
            s = s[: p] + s[p:][::-1]
            if check():
                print(p)
            else:
                print(-1)
            return
        
        if x > k:
            operation(n)
        elif x == k:
            p = n
            for i in range(n - k - 1, -1, -1):
                if s[i] == s[i + k]:
                    p = i + 1
                    break
            operation(p)
        else:
            flag = False
            i = 0
            while i < n:
                if s[i] != s[-1]:
                    i += 1
                    continue
                j = i
                while j + 1 < n and s[i] == s[j + 1]:
                    j += 1
                if j - i + 1 + x == k:
                    operation(j + 1)
                    flag = True
                    break
                elif j - i + 1 + x - k == k:
                    operation(i + k - x)
                    flag = True
                    break
                i = j + 1
            if not flag:
                operation(n)
    
    return


def main():
    D()
    return


if __name__ == '__main__':
    main()
