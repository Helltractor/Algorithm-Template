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
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List, Tuple
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
        s = I()
        n = II()
        a = [I() for i in range(n)]
        ans = []
        def dfs(i, li):
            if len(set(li)) < len(li):
                return 10 ** 18
            if i == len(s):
                if len(ans):
                    if len(li) < len(ans[0]):
                        ans.clear()
                        ans.append(li)
                else:
                    ans.append(li)
                return 0
            if i > len(s):
                return 10 ** 18
            res = 10 ** 18
            for j in range(n):
                for k in range(i - len(a[j]) + 1, i + 1):
                    if s[k: k + len(a[j])] == a[j] and k + len(a[j]) > i:
                        res = min(res, dfs(k + len(a[j]), li + [(j + 1, k + 1)]))
            return res
        dfs(0, [])
        if len(ans):
            print(len(ans[0]))
            for x, y in ans[0]:
                print(x, y)
        else:
            print(-1)
    return

# def cf1714D(T: int, tests: List[Tuple[str, int, List[str]]]) -> List[List[Tuple[int, int]]]:
#     results = []
#     for test in tests:
#         t, n, a = test
#         f = [1e9] * (len(t) + 1)
#         f[0] = 0
#         from_ = [(0, 0)] * (len(t) + 1)
#         for i in range(1, len(t) + 1):
#             for j, s in enumerate(a):
#                 m = len(s)
#                 for k in range(max(i - m, 0), min(i, len(t) - m + 1)):
#                     if t[k: k+m] == s and f[k] + 1 < f[i]:
#                         f[i] = f[k] + 1
#                         from_[i] = (k, j + 1)
#         if f[len(t)] == 1e9:
#             results.append([])
#             continue
#         i = len(t)
#         res = []
#         while from_[i][0] > 0:
#             res.append((from_[i][1], from_[i][0] + 1))
#             i = from_[i][0]
#         res.append((from_[i][1], 1))
#         results.append(res[::-1])
#     return results
#
# def main():
#     T = II()
#     tests = []
#     for _ in range(T):
#         t = I()
#         n = II()
#         a = [I() for _ in range(n)]
#         tests.append((t, n, a))
#     results = cf1714D(T, tests)
#     for res in results:
#         if not res:
#             print(-1)
#         else:
#             print(len(res))
#             for r in res:
#                 print(*r)

if __name__ == "__main__":
    main()