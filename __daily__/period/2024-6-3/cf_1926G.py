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

# https://codeforces.com/contest/1926/problem/G
#
# 输入 T(≤1e3) 表示 T 组数据。所有数据的 n 之和 ≤1e5。
# 每组数据输入 n(2≤n≤1e5) 和 n-1 个数 a2,a3,...,an (1≤ai<i)，表示节点 i 和节点 ai 之间有一条无向边。
# 这 n-1 条无向边形成了一棵树，节点编号从 1 到 n。
# 然后输入长为 n 的字符串 s，只包含字母 P S C，表示节点 i 的类型是 s[i]。
#
# 最少要切断多少条边，使得类型为 P 的节点都无法到达任意类型为 S 的节点？

def cf_1926G():
    for _ in range(II()):
        n = II()
        a = [0, 0] + LII()
        s = I()
        f = [[0, 0] for _ in range(n + 1)]
        for i in range(n, 0, -1):
            g = f[i][:]
            if s[i - 1] != 'C':
                g[ord(s[i - 1]) & 1] = 1e9
            f[a[i]][0] += min(g[0], g[1] + 1)
            f[a[i]][1] += min(g[1], g[0] + 1)
        print(min(f[0]))
    return


def main():
    cf_1926G()
    return


if __name__ == '__main__':
    main()
