# _*_ coding: utf-8 _*_
# @File : graph.py
# @Time : 2023/11/21 18:23
# @Author : Helltrackor
from typing import List


def undirected_graph(n: int, matrix: List[List]):
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    out_degree = [0] * n
    for x, y in matrix:
        graph[x].append(y)
        graph[y].append(x)
        in_degree[x] += 1
        in_degree[y] += 1
        out_degree[x] += 1
        out_degree[y] += 1
    return graph, in_degree, out_degree


def directed_graph(n: int, matrix: List[List]):
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    out_degree = [0] * n
    for x, y in matrix:
        graph[x].append(y)
        in_degree[y] += 1
        out_degree[y] += 1
    return graph, in_degree, out_degree
