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

class Comb:
    
    def __init__(self):
        self.mod = MOD
        self.l = 3 * pow(10, 5) + 5
        self.fact = [1] * (self.l + 1)
        self.inv = [1] * (self.l + 1)
        for i in range(1, self.l + 1):
            self.fact[i] = self.fact[i - 1] * i % self.mod
        self.inv[self.l] = pow(self.fact[self.l], self.mod - 2, self.mod)
        for i in range(self.l - 1, -1, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod
    
    def comb(self, n, r):
        return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0
    
# https://codeforces.com/problemset/problem/1400/G
#
# 输入 n(1≤n≤3e5) 和 m(0≤m≤min(20,n*(n-1)/2))。
# 解释：有 n 个雇佣兵，从中选择一些人（至少一个人），组成一支部队。m 的含义见下。
#
# 然后输入 n 个闭区间的左右端点 [Li,Ri]，范围 [1,n]。
# 解释：如果选了第 i 位雇佣兵，那么部队的人数必须在闭区间 [Li,Ri] 中。
#
# 最后输入 m 对数字 (ai, bi)，满足 1≤ai<bi≤n。
# 解释：这 m 对雇佣兵相互憎恨，如果选了第 ai 位雇佣兵，那么不能选第 bi 位雇佣兵，反之亦然。
#
# 输出有多少种选法，模 998244353。

def cf_1400G():
    cb = Comb()
    n, m = MII()
    a = [LII() for _ in range(n)]
    b = [LII() for _ in range(m)]
    diff = [0] * (n + 2)
    sum = [[0] * 41 for _ in range(n + 1)]
    for l, r in a:
        diff[l] += 1
        diff[r + 1] -= 1
    cnt = 0
    for i in range(1, n + 1):
        cnt += diff[i]
        for j in range(41):
            sum[i][j] = (sum[i - 1][j] + cb.comb(cnt - j, i - j)) % MOD
    ans = sum[n][0]
    has = [0] * (n + 1)
    for i in range(1, 1 << m):
        l, r, k = 1, n, 0
        for j in range(m):
            if i >> j & 1:
                # 计算区间交集
                p = b[j]
                l = max(l, a[p[0] - 1][0], a[p[1] - 1][0])
                r = min(r, a[p[0] - 1][1], a[p[1] - 1][1])
                # 时间戳，记录是否已经访问过
                if has[p[0]] != i:
                    has[p[0]] = i
                    k += 1
                if has[p[1]] != i:
                    has[p[1]] = i
                    k += 1
        if r < l:
            continue
        res = sum[r][k] - sum[l - 1][k]
        if bin(i).count('1') & 1:
            res = -res
        ans += res
    print((ans % MOD + MOD) % MOD)
    
    return


def main():
    cf_1400G()
    return


if __name__ == '__main__':
    main()
