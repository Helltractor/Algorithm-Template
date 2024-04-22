# _*_ coding: utf-8 _*_
# @File : comb.py
# @Time : 2024/4/22 10:40
# @Author : Helltractor

# template for calculating combination number
"""
mod = pow(10, 9) + 7
l = 3 * pow(10, 5) + 5
fact = [1] * (l + 1)
for i in range(1, l + 1):
    fact[i] = i * fact[i - 1] % mod
inv = [1] * (l + 1)
inv[l] = pow(fact[l], mod - 2, mod)
for i in range(l - 1, -1, -1):
    inv[i] = (i + 1) * inv[i + 1] % mod
def comb(n, r):
    return fact[n] * inv[r] % mod * inv[n - r] % mod if n >= r >= 0 else 0
"""

mod = pow(10, 9) + 7  # 定义模数
l = 3 * pow(10, 5) + 5  # 定义上限
fact = [1] * (l + 1)  # 初始化阶乘列表
for i in range(1, l + 1):
    fact[i] = i * fact[i - 1] % mod  # 计算阶乘并取模

inv = [1] * (l + 1)  # 初始化模逆元列表
inv[l] = pow(fact[l], mod - 2, mod)  # 计算最大阶乘的模逆元
for i in range(l - 1, -1, -1):
    inv[i] = (i + 1) * inv[i + 1] % mod  # 计算其他阶乘的模逆元

# 计算组合数 C(n, r)
def comb(n, r):
    # 计算组合数 C(n, r)，如果 n >= r >= 0 则返回结果，否则返回 0
    return fact[n] * inv[r] % mod * inv[n - r] % mod if n >= r >= 0 else 0