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
	
def qpow(x, y):
	res = 1
	while y:
		if y & 1:
			res = res * x
		x = x * x
		y >>= 1
	return res

def cf_453A():
	n, m = map(int, input().split())
	ans = n
	for i in range(1, n):
		# ans += i * (pow(i / n, m) - pow((i - 1) / n, m))
		ans -= pow(i / n, m)
	print(ans)
	return


def main():
	# start = time.time()
	cf_453A()
	# print(time.time() - start)
	return


if __name__ == '__main__':
	main()
