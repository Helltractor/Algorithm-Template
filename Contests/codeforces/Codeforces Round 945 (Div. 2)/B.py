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

def cf_B_TLE():
	for _ in range(II()):
		n = II()
		a = LII()
		arr = [[0] * 20  for _ in range(n + 1)]
		for i in range(n):
			x = a[i]
			for j in range(20):
				if x >> j & 1:
					arr[i + 1][j] += 1
				arr[i + 1][j] += arr[i][j]
		ans = n
		print(arr)
		for k in range(1, n):
			flag = True
			for i in range(1, n - k + 1):
				for j in range(20):
					if arr[k][j]:
						if arr[i + k][j] - arr[i][j] == 0:
							flag = False
							break
					else:
						if arr[i + k][j] - arr[i][j] != 0:
							flag = False
							break
				if not flag:
					break
			if flag:
				ans = k
				break
		print(ans)
	
	return

def check(arr, n, k):
	flag = True
	for i in range(1, n - k + 1):
		for j in range(20):
			if arr[k][j]:
				if arr[i + k][j] - arr[i][j] == 0:
					flag = False
					break
			else:
				if arr[i + k][j] - arr[i][j] != 0:
					flag = False
					break
		if not flag:
			return False
	return True
	
def cf_B_BinarySearch():
	for _ in range(II()):
		n = II()
		a = LII()
		arr = [[0] * 20  for _ in range(n + 1)]
		for i in range(n):
			x = a[i]
			for j in range(20):
				if x >> j & 1:
					arr[i + 1][j] += 1
				arr[i + 1][j] += arr[i][j]
		
		l = 1
		r = n
		while l <= r:
			m = l + r >> 1
			if check(arr, n, m):
				r = m - 1
			else:
				l = m + 1
		print(l)
	return
	
def cf_B():
	for _ in range(II()):
		n = II()
		a = LII()
		mx = max(a)
		arr = [[0] * mx.bit_length() for _ in range(n)]
		for i in range(n):
			for j in range(mx.bit_length()):
				if a[i] >> j & 1:
					arr[i][j] += 1
		mat = list(zip(*arr))
		ans = 1
		for row in mat:
			cnt = 0
			tmp = 0
			for x in row:
				if x == 0:
					tmp += 1
				else:
					cnt = max(cnt, tmp)
					tmp = 0
			if tmp == len(row):
				continue
			cnt = max(cnt, tmp)
			ans = max(cnt + 1, ans)
		print(ans)
	return


def main():
	cf_B_BinarySearch()
	return


if __name__ == '__main__':
	main()
