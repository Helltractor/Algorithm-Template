# _*_ coding: utf-8 _*_
# @File : primes_linear.py
# @Time : 2024/5/9 17:24
# @Author : Helltractor
# @Description : 线性筛

# primes = []
# is_prime = [True] * n
# # is_prime = [False] * 2 + [True] * (n - 2)
# for i in range(2, n):
#     if is_prime[i]:
#         primes.append(i)
#     for p in primes:
#         if i * p >= n: break
#         is_prime[i * p] = False
#         if i % p == 0: break
# primes.extend([n, n])   # 防止下标越界

class Linear:

    def primes_linear(n: int) -> int:
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:  break
                is_prime[i * p] = False
                if i % p == 0:  break
        return primes