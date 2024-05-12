# _*_ coding: utf-8 _*_
# @File : comb.py
# @Time : 2024/4/22 10:40
# @Author : Helltractor
# @Description : Combination number

# mod = pow(10, 9) + 7
# l = 3 * pow(10, 5) + 5
# fact = [1] * (l + 1)
# inv = [1] * (l + 1)
# inv[l] = pow(fact[l], mod - 2, mod)
# for i in range(l):
#     fact[i + 1] = i * fact[i] % mod
#     inv[l - i - 1] = inv[l - i] * (l - i) % mod
# def comb(n, r):
#     return fact[n] * inv[r] % mod * inv[n - r] % mod if n >= r >= 0 else 0

class Comb:
    
    def __init__(self):
        self.mod = pow(10, 9) + 7
        self.l = 3 * pow(10, 5) + 5
        self.fact = [1] * (self.l + 1)
        self.inv = [1] * (self.l + 1)
        self.inv[self.l] = pow(self.fact[self.l], self.mod - 2, self.mod)
        for i in range(self.l):
            self.fact[i + 1] = i * self.fact[i] % self.mod
            self.inv[self.l - i - 1] = self.inv[self.l - i] * (self.l - i) % self.mod

    def comb(self, n, r):
        return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0