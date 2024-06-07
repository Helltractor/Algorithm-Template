# _*_ coding: utf-8 _*_
# @File : difference.py
# @Time : 2023/9/29 16:52
# @Author : Helltrackor
from typing import List


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/FfMCgb/
# 你有一个长为 n 的数组 a，一开始所有元素均为 0。
# 给定一些区间操作，其中 queries[i] = [left, right, x]，
# 你需要把子数组 a[left], a[left+1], ... a[right] 都加上 x。
# 返回所有操作执行完后的数组 a。

def diff_array(n: int, queries: List[List[int]]) -> List[int]:
    diff = [0] * n  # 差分数组
    for left, right, x in queries:
        diff[left] += x
        if right + 1 < n:
            diff[right + 1] -= x
    for i in range(1, n):
        diff[i] += diff[i - 1]  # 直接在差分数组上复原数组 a
    return diff


def diff_array_(n: int, queries: List[List[int]]) -> List[int]:
    diff = [0] * (n + 1)  # 差分数组
    for left, right, x in queries:
        diff[left] += x
        diff[right + 1] -= x
    for i in range(1, n):
        diff[i] += diff[i - 1]  # 直接在差分数组上复原数组 a
    return diff[:-1]
