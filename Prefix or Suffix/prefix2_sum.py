# _*_ coding: utf-8 _*_
# @File : prefix2_sum.py
# @Time : 2023/12/14 13:13
# @Author : Helltractor
from typing import List


class prefix_sum:
    # 二维前缀和
    def __init__(self, mat: List[List[int]]):
        m, n = len(mat), len(mat[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        pre = self.pre
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + mat[i - 1][j - 1]

    # 查询以(r1,c1)为左上角，(r2,c2)为右下角的矩形区间内所有值的和
    def find(self, r1: int, c1: int, r2: int, c2: int) -> int:
        pre = self.pre
        return pre[r2 + 1][c2 + 1] - pre[r2 + 1][c1] - pre[r1][c2 + 1] + pre[r1][c1]


class prefix_sum_:
    # 二维前缀和
    def __init__(self, mat: List[List[int]]):
        m, n = len(mat), len(mat[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        pre = self.pre
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + v

    # 查询以(r1,c1)为左上角，(r2,c2)为右下角的矩形区间内所有值的和
    def find(self, r1: int, c1: int, r2: int, c2: int) -> int:
        pre = self.pre
        return pre[r2 + 1][c2 + 1] - pre[r2 + 1][c1] - pre[r1][c2 + 1] + pre[r1][c1]
