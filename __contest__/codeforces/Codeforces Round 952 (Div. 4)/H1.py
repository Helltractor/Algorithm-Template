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

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = [1] * n
        self.size = [1] * n
        self.n = n

    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]

    def union_rank(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


def H1():
    for _ in range(II()):
        n, m = MII()
        a = [I() for _ in range(n)]
        uf = UnionFind(n * m)
        for i in range(n):
            for j in range(m):
                if a[i][j] == '#':
                    if i and a[i - 1][j] == '#':
                        uf.union_by_size(i * m + j, (i - 1) * m + j)
                    if j and a[i][j - 1] == '#':
                        uf.union_by_size(i * m + j, i * m + j - 1)
                
        ans = 0
        for i in range(n):
            d = dict()
            d[-1] = 0
            cnt = 0
            for j in range(m):
                if a[i][j] == '.':
                    cnt += 1
                else:
                    tmp = uf.find(i * m + j)
                    d[tmp] = uf.size[tmp]
                if i and a[i - 1][j] == '#':
                    tmp = uf.find((i - 1) * m + j)
                    d[tmp] = uf.size[tmp]
                if i < n - 1 and a[i + 1][j] == '#':
                    tmp = uf.find((i + 1) * m + j)
                    d[tmp] = uf.size[tmp]
            ans = max(ans, sum(d.values()) + cnt)
        for j in range(m):
            d = dict()
            d[-1] = 0
            cnt = 0
            for i in range(n):
                if a[i][j] == '*':
                    cnt += 1
                else:
                    tmp = uf.find(i * m + j)
                    d[tmp] = uf.size[tmp]
                if j and a[i][j - 1] == '#':
                    tmp = uf.find(i * m + j - 1)
                    d[tmp] = uf.size[tmp]
                if j < m - 1 and a[i][j + 1] == '#':
                    tmp = uf.find(i * m + j + 1)
                    d[tmp] = uf.size[tmp]
            ans = max(ans, sum(d.values()) + cnt)
        print(ans)
    return

def main():
    H1()
    return


if __name__ == '__main__':
    main()
