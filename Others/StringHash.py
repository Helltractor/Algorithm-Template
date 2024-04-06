# _*_ coding: utf-8 _*_
# @File : StringHash.py
# @Time : 2024/3/11 15:50
# @Author : Helltractor

class StringHash:
    # 字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值
    def __init__(self, s):
        n = len(s)
        self.BASE = BASE = 131313  # 进制 31,131,13131,13331,131313
        self.MOD = MOD = 10 ** 13 + 7  # 10**13+37 ,10**13+51 ,10**13+99 ,10**13+129 ,10**13+183
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE + ord(s[i - 1])) % MOD

    # 用O(1)时间获取闭区间[l,r]（即s[l:r]）的哈希值，比切片要快
    def get_hash(self, l, r):
        return (self.h[r + 1] - self.h[l] * self.p[r - l + 1]) % self.MOD

    # 获取 s[l1:r1+1] 和 s[l2:r2+1] 拼接的哈希值，要求不能有重叠部分，且有先后顺序
    def get_addhash(self, l1, r1, l2, r2):
        return (self.get_hash(l1, r1) * self.p[r2 - l2 + 1] + self.get_hash(l2, r2)) % self.MOD


class Hash:
    def __init__(self, s, seed=31, mod=10 ** 13 + 7):
        self.n = len(s)
        self.pw = [1]
        self.mod = mod
        self.table = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.pw.append(self.pw[-1] * seed % mod)

        for i in range(self.n - 1, -1, -1):
            self.table[i] = self.table[i + 1] * seed + ord(s[i])
            self.table[i] %= mod

    # 取闭区间[l,r] 可以 l == r + 1 返回0
    def get(self, l, r):
        return (self.table[l] - self.table[r + 1] * self.pw[r - l + 1] + self.mod) % self.mod