# _*_ coding: utf-8 _*_
# @File : difference_2D.py
# @Time : 2023/12/14 13:20
# @Author : Helltractor

class Difference2D:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.diff = [[0] * (n + 2) for _ in range(m + 2)]

    def add(self, r1, c1, r2, c2, c):  # 下标从0开始，区间+c
        diff = self.diff
        diff[r1 + 1][c1 + 1] += c
        diff[r1 + 1][c2 + 2] -= c
        diff[r2 + 2][c1 + 1] -= c
        diff[r2 + 2][c2 + 2] += c

    def get(self):  # 还原
        diff = self.diff
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff
