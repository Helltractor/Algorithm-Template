# _*_ coding: utf-8 _*_
# @File : UnionFind.py
# @Time : 2023/11/25 17:08
# @Author : Helltrackor

# 链接：https://zhuanlan.zhihu.com/p/93647900
"""
class UF:
    def __init__(self, n: int):
        self.parent = {i: i for i in range(1, n+1)}
        self.rank = {i: 1 for i in range(1, n+1)}

    # 查询
    def find(self, x: int):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    # 查询（路径压缩）
    def find(self, x: int):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 查询（路径压缩，简写）
    def find(self, x: int):
        return x if x == self.parent[x] \
            else self.parent[x] = self.find(self.parent[x])

    # 合并
    def union(self, i: int, j: int):
        self.parent[self.find(i)] = self.find(j)

    # 合并（按秩合并）
    def union(self, i: int, j: int):
        x, y = self.find(i), self.find(j)
        if self.rank[x] <= self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y] and x != y:
            self.rank[y] += 1

    # 连通性
    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)

    # 添加结点
    def add(self, x):
        self.parent[x] = None
"""


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = [1] * n
        self.size = [1] * n
        self.n = n

    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]

    def union_rank(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.n = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]

    def union_rank(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


# 作者：Hao Kun Yang
# 链接：https://leetcode.cn/problems/evaluate-division/solutions/549058/pythonbing-cha-ji-fu-mo-ban-by-milomusia-kfsu/
class UnionFind1:
    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.parent = {}

    # 迭代法
    def find(self, x):
        """
        查找根节点
        路径压缩
        """
        root = x
        # 查找根节点
        while self.parent[root] is not None:
            root = self.parent[root]

        # 路径压缩
        while x != root:
            original_parent = self.parent[x]
            self.parent[x] = root
            x = original_parent

        return root

    def union(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y

    def is_connected(self, x, y):
        """
        判断两节点是否相连
        """
        return self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点
        """
        if x not in self.parent:
            self.parent[x] = None


class UnionFind2:
    def __init__(self, parent):
        self.parent = parent
        self.rank = [1] * len(parent)
        self.size = [1] * len(parent)

    # 直接查找
    def find_direct(self, x):
        if self.parent[x] == x:
            return x
        return self.find_direct(self.parent[x])

    # 带路径压缩的查找
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 直接求并
    def union_direct(self, x, y):
        x_root, y_root = self.find_direct(x), self.find_direct(y)
        if x_root != y_root:
            self.parent[y_root] = x_root

    # 按大小求并
    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]

    # 按秩求并
    def union_rank(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1


# 简洁版
p = list(range(n))


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    p[find(y)] = find(x)


def connected(x, y):
    return find(x) == find(y)