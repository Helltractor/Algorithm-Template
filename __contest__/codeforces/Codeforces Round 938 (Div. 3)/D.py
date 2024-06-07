ImportType = 1
InputType = 1
ConstType = 1
if ImportType:
    import os, sys, random, threading
    # sys.exit() 退出程序
    # sys.setrecursionlimit(10**6) #调整栈空间
    from random import randint, choice, shuffle
    # randint(a,b)从[a,b]范围随机选择一个数
    # choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
    # shuffle(x)将一个可变的序列x中的元素打乱
    from copy import deepcopy
    from io import BytesIO, IOBase
    from types import GeneratorType
    from functools import lru_cache, reduce
    # reduce(op,迭代对象)
    from bisect import bisect_left, bisect_right
    # bisect_left(x) 大于等于x的第一个下标
    # bisect_right(x) 大于x的第一个下标
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    # accumulate(a)用a序列生成一个累积迭代器，一般list化前面放个[0]做前缀和用
    # combinations(a,k)a序列选k个 组合迭代器
    # permutations(a,k)a序列选k个 排列迭代器
    from heapq import heapify, heappop, heappush
    # heapify将列表转为堆
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    # 小写字母，大写字母，十进制数字
    from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    # ceil向上取整，floor向下取整 ，sqrt开方 ，factorial阶乘
    from decimal import Decimal, getcontext
    # Decimal(s) 实例化Decimal对象,一般使用字符串
    # getcontext().prec=100 修改精度
    from sys import stdin, stdout, setrecursionlimit

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")


    def I():
        return input()


    def II():
        return int(input())


    def MII():
        return map(int, input().split())


    def LI():
        return list(input().split())


    def LII():
        return list(map(int, input().split()))


    def GMI():
        return map(lambda x: int(x) - 1, input().split())


    def LGMI():
        return list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353


def main():
    for _ in range(II()):
        n, m, k = MII()
        a = LII()
        b = LII()
        cnt = Counter(b)
        delta = 0
        for i in range(m):
            if a[i] in cnt:
                if cnt[a[i]] > 0:
                    delta += 1
                cnt[a[i]] -= 1
        ans = int(delta >= k)
        for i in range(m, n):
            if a[i - m] in cnt:
                if cnt[a[i - m]] >= 0:
                    delta -= 1
                cnt[a[i - m]] += 1
            if a[i] in cnt:
                if cnt[a[i]] > 0:
                    delta += 1
                cnt[a[i]] -= 1
            ans += int(delta >= k)
        print(ans)
    return


main()