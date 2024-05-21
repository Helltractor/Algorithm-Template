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


def cf_D():
	for _ in range(II()):
		n = II()
		s = I()
		w = {'N': 0, 'S': 0, 'E': 1, 'W': 1}
		ans = list(s)
		ok = 0
		for i, c in enumerate(s):
			ans[i] = 'H' if w[c] == 0 else 'R'
			if ans[i] == 'H': ok |= 1
			if ans[i] == 'R': ok |= 2
			w[c] ^= 1
		if ok == 3 and w['N'] == w['S'] and w['E'] == w['W']:
			print(''.join(ans))
		else:
			print('NO')
	return


def main():
	cf_D()
	return


if __name__ == '__main__':
	main()
