# _*_ coding: utf-8 _*_
# @File : BinaryIndexedTree.py
# @Time : 2023/11/13 14:42
# @Author : Helltrackor

"""
    树状数组，也称作“二叉索引树”（Binary Indexed Tree）或 Fenwick 树。 它可以高效地实现如下两个操作：

    单点更新 update(x,delta)： 把序列 x 位置的数加上一个值 delta(x > 0)；
    前缀和查询 query(x)：查询序列 [1,...x] 区间的区间和，即位置 x 的前缀和。
    这两个操作的时间复杂度均为 O(logn)。

    树状数组最基本的功能就是求比某点 x 小的点的个数（这里的比较是抽象的概念，可以是数的大小、坐标的大小、质量的大小等等）。
"""


# class BinaryIndexedTree:
#     __slots__ = ["n", "c"]
#
#     def __init__(self, n):
#         self.n = n
#         self.c = [0] * (n + 1)
#
#     def update(self, x: int, delta: int):
#         while x <= self.n:
#             self.c[x] += delta
#             x += x & -x
#
#     def query(self, x: int) -> int:
#         s = 0
#         while x > 0:
#             s += self.c[x]
#             x -= x & -x
#         return s

class BinaryIndexedTree:
    __slots__ = ["n", "c"]

    def __init__(self, n):
        """
        初始化树状数组对象

        Args:
        - n: 数组的大小，即树状数组的长度
        """
        self.n = n
        self.c = [0] * (n + 1)  # 初始化树状数组，长度为 n+1，下标从 1 开始

    def update(self, x: int, delta: int):
        """
        更新操作：在数组位置 x 处加上 delta

        Args:
        - x: 要更新的位置
        - delta: 要加上的值
        """
        while x <= self.n:
            self.c[x] += delta  # 更新当前位置的值
            x += x & -x  # 利用 x 的二进制表示中的最低非零位，找到下一个需要更新的位置

    def query(self, x: int) -> int:
        """
        查询操作：计算前 x 个元素的和

        Args:
        - x: 查询的范围

        Returns:
        - 前 x 个元素的和
        """
        s = 0
        while x > 0:
            s += self.c[x]  # 累加当前位置的值
            x -= x & -x  # 利用 x 的二进制表示中的最低非零位，找到下一个需要累加的位置
        return s


if __name__ == "__main__":
    # 使用示例
    n = 8
    bit_tree = BinaryIndexedTree(n)

    # 迭代更新
    for i in range(1, n + 1):
        bit_tree.update(i, 1)

    # 查询操作
    result = bit_tree.query(5)
    print(result)  # 输出：5