ImportType = 1
InputType = 1
ConstType = 1
if ImportType:
	import os, sys, random, threading
	from random import randint, choice, shuffle
	from copy import deepcopy
	from io import BytesIO, IOBase
	from types import GeneratorType
	from functools import lru_cache, reduce
	from bisect import bisect_left, bisect_right
	from collections import Counter, defaultdict, deque
	from itertools import accumulate, combinations, permutations
	from heapq import heapify, heappop, heappush, heappushpop
	from typing import Generic, Iterable, Iterator, TypeVar, Union, List
	from string import ascii_lowercase, ascii_uppercase, digits
	from math import ceil, comb, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
	from decimal import Decimal, getcontext
	from sys import stdin, stdout, setrecursionlimit

if InputType:
	input = lambda: sys.stdin.readline().rstrip("\r\n")
	I = lambda: input()
	II = lambda: int(input())
	MII = lambda: map(int, input().split())
	LI = lambda: list(input().split())
	LII = lambda: list(map(int, input().split()))
	GMI = lambda: map(lambda x: int(x) - 1, input().split())
	LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
	RD = random.randint(10 ** 9, 2 * 10 ** 9)
	MOD = 998244353
	Y = "Yes"
	N = "No"

def prime_factors(n):
	i = 2
	factors = Counter()
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors[i] += 1
	if n > 1:
		factors[n] += 1
	return factors

def cf_1884D():
	for _ in range(II()):
		n = II()
		a = LII()
		cnt = [0] * (n + 1)
		for x in a:
			cnt[x] += 1
		hasD = [False] * (n + 1)
		res = [0] * (n + 1)
		for i in range(n, 0, -1):
			c = 0
			for j in range(i, n + 1, i):
				if cnt[i] > 0:
					hasD[j] = True
				c += cnt[j]
				res[i] -= res[j]
			res[i] += c * (c - 1) // 2
		print(sum(res[i] if not hasD[i] else 0 for i in range(1, n + 1)))
	return


def main():
	cf_1884D()
	return


if __name__ == '__main__':
	main()
