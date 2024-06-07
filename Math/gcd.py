# _*_ coding: utf-8 _*_
# @File : greatest_common_divisor.py
# @Time : 2023/11/16 14:44
# @Author : Helltrackor

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


def lcm(a, b):
    return a * b // gcd(a, b)
