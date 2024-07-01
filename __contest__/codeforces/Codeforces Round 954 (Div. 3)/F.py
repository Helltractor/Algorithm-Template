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
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bridgeUtil(self, u, visited, parent, low, disc, bridges):
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc, bridges)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    def findBridges(self):
        visited = [False] * (self.V + 1)
        disc = [float('Inf')] * (self.V + 1)
        low = [float('Inf')] * (self.V + 1)
        parent = [-1] * (self.V + 1)
        bridges = []
        
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.bridgeUtil(i, visited, parent, low, disc, bridges)
        
        return bridges
    
    def dfsCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.dfsCount(i, visited)
        return count
    
    def minRemoveEdge(self):
        bridges = self.findBridges()
        min_pairs = float('Inf')
        
        for u, v in bridges:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
            
            visited = [False] * (self.V + 1)
            size1 = self.dfsCount(u, visited)
            size2 = self.V - size1
            
            min_pairs = min(min_pairs, size1 * (size1 - 1) // 2 + size2 * (size2 - 1) // 2)
            
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        return min_pairs
    
def F():
    for _ in range(II()):
        n, m = MII()
        g = Graph(n)
        for _ in range(m):
            u, v = GMI()
            g.addEdge(u, v)
        print(g.minRemoveEdge())
        
        
        
    return


def main():
    F()
    return


if __name__ == '__main__':
    main()
