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
    
# https://codeforces.com/problemset/problem/1950/F
#
# 输入 T(≤1e4) 表示 T 组数据。所有数据的 a+b+c 之和 ≤3e5。
# 每组数据输入 a,b,c (0≤a,b,c≤1e5 且 1≤a+b+c)。
#
# 有一棵二叉树，其中 a 个节点有两个儿子，b 个节点有一个儿子，c 个节点没有儿子。
# 输出这棵二叉树的最小高度。
# 注意这里的高度是根到最远叶节点的路径上的边的个数。
# 特别地，只有一个节点的二叉树的高度为 0。
#
# 进阶：做到 O(1) 时间。

def F():
    for _ in range(II()):
        a, b, c = MII()
    
        if a:
            n = len(bin(a)) - 3
            a -= (1 << n) - 1
            ans = n + (a > 0)
            leaf = (1 << n) + a
            if b + c < leaf or c != leaf:
                print(-1)
            else:
                ans += ceil((b - leaf + 2 * a) / leaf)
                print(ans)
        else:
            if c != 1:
                print(-1)
            else:
                print(b)
    return


def main():
    F()
    return


if __name__ == '__main__':
    main()
