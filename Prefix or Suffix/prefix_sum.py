# _*_ coding: utf-8 _*_
# @File : prefix_sum.py
# @Time : 2024/1/17 15:47
# @Author : Helltractor
from math import sqrt
from typing import *


def prefix_sum(nums: List[int]) -> None:
    # 获取数组的长度
    n = len(nums)
    sqr = int(sqrt(n)) + 1

    # 计算前缀和数组
    # from itertools import accumulate
    # pre = accumulate(nums, initial=0)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + nums[i]

    # 计算不同步长划分前缀和数组
    step_pre = [[0] * (n + sqr) for _ in range(n)]
    for d in range(1, n):
        for i in range(n):
            step_pre[d][d + i] = step_pre[d][i] + nums[i]

    # 计算带权重的前缀和数组，权重为 1, 2, ..., n
    weighted_pre = [0] * (n + 1)
    for i in range(n):
        weighted_pre[i + 1] = weighted_pre[i] + (i // 1 + 1) * nums[i]

    # 计算带权重和不同步长的前缀和数组
    weighted_step_pre = [[0] * (n + sqr) for _ in range(n)]
    for d in range(1, n):
        for i in range(n):
            weighted_step_pre[d][d + i] = weighted_step_pre[d][i] + (i // d + 1) * nums[i]


# link: https://codeforces.com/contest/1921/problem/F
def solve():
    # int(input())
    # list(map(int, input().split()))
    from math import sqrt

    for _ in range(int(input())):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        ret = []
        m = int(sqrt(n)) + 1
        s1 = [[0] * (n + m) for _ in range(m)]
        s2 = [[0] * (n + m) for _ in range(m)]
        for i in range(1, m):
            for j in range(n):
                s1[i][i + j] = s1[i][j] + a[j]
                s2[i][i + j] = s2[i][j] + a[j] * (j // i + 1)

        for _ in range(q):
            s, d, k = map(int, input().split())
            tmp = 0
            s -= 1
            if d < m:
                r = s + d * k
                tmp = s2[d][r] - s2[d][s] - (s1[d][r] - s1[d][s]) * (
                        s // d)  # s2[r+d] - s2[l] - (s1[r+d] - s[l]) * (s // d)
            else:
                for i in range(k):
                    tmp += a[s + d * i] * (i + 1)
            ret.append(tmp)
        print(*ret)


if __name__ == "__main__":
    solve()
