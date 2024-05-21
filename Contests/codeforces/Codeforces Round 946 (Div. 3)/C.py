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


def cf_C():
	for _ in range(II()):
		n = II()
		a = LII()
		ans = 0
		dx = defaultdict(int)
		dy = defaultdict(int)
		dz = defaultdict(int)
		vis = defaultdict(int)
		for i in range(n - 2):
			j = i + 1
			k = i + 2
			fx = (a[i], a[k])
			fy = (a[i], a[j])
			fz = (a[j], a[k])
			ans += dx[fx] + dy[fy] + dz[fz]
			v = (a[i], a[j], a[k])
			ans -= vis[v] * 3
			vis[v] += 1
			dx[fx] += 1
			dy[fy] += 1
			dz[fz] += 1
	
		print(ans)
	return


def main():
	cf_C()
	return


if __name__ == '__main__':
	main()
