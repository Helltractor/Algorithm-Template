# _*_ coding: utf-8 _*_
# @File : power.py
# @Time : 2023/11/30 19:57
# @Author : Helltractor

# 快速幂（迭代版）
def fast_power(x: int, y: int, z: int = 1) -> float:
    """
        Args:
            x: 底数
            y: 指数
            z: MOD
        Returns: 幂指数
    """
    ret = 1.0
    while y:
        if y % 2:
            ret = ret * x % z
        x = x * x % z
        y //= 2
    return ret

# 快速幂（递归版）
def fast_power_rec(x: int, y: int, z: int = 1) -> float:
    if y == 0:
        return 1.0
    ret = fast_power_rec(x, y // 2) % z
    return ret * ret % z if y % 2 == 0 else ret * ret * x % z


def myPow(x: float, n: int) -> float:
    return fast_power(x, n) if n >= 0 else 1.0 / fast_power(x, -n)
