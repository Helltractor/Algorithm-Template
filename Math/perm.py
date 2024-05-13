# _*_ coding: utf-8 _*_
# @File : perm.py
# @Time : 2024/5/13 下午10:32
# @Author : Helltractor

# mod = pow(10, 9) + 7
# l = 3 * pow(10, 5) + 5
# fact = [1] * (l + 1)
# inv = [1] * (l + 1)
# inv[l] = pow(fact[l], mod - 2, mod)
# for i in range(l):
# 	fact[i + 1] = i * fact[i] % mod
# 	inv[l - i - 1] = inv[l - i] * (l - i) % mod
# def perm(n, r):
# 	return fact[n] * inv[n - r] % mod if n >= r >= 0 else 0

class Perm:
	
	def __init__(self):
		self.factorial = [1] * (l + 1)
		self.inverse = [1] * (l + 1)
		self.inverse[l] = pow(self.factorial[l], mod - 2, mod)
		for i in range(l):
			self.factorial[i + 1] = i * self.factorial[i] % mod
			self.inverse[l - i - 1] = self.inverse[l - i] * (l - i) % mod
		
	def perm(self, n, r):
		return self.factorial[n] * self.inverse[n - r] % mod if n >= r >= 0 else 0
