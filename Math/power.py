# _*_ coding: utf-8 _*_
# @File : power.py
# @Time : 2023/11/30 19:57
# @Author : Helltractor

# 快速幂（迭代版）
def fast_power(x: int, y: int, mod: int = 31) -> float:
    ans = 1.0
    while y:
        if y % 2:
            ans = ans * x % mod
        x = x * x % mod
        y //= 2
    return ans

# 快速幂（递归版）
def fast_power_rec(x: int, y: int, mod: int = 31) -> float:
    if y == 0:
        return 1.0
    ans = fast_power_rec(x, y // 2) % mod
    return ans * ans % mod if y % 2 == 0 else ans * ans * x % mod


def myPow(x: float, n: int) -> float:
    return fast_power(x, n) if n >= 0 else 1.0 / fast_power(x, -n)
