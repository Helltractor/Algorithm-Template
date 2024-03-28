# _*_ coding: utf-8 _*_
# @File : SegmentTree.py
# @Time : 2023/12/16 21:09
# @Author : Helltractor
"""
    作者：Benhao
    链接：https://leetcode.cn/problems/range-module/solutions/1612783/by-himymben-vo9g/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = False  # bool类型
        self.add = False  # lazy标记


class SegmentTree:
    __slots__ = 'root'

    def __init__(self):
        self.root = Node()

    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: bool) -> None:
        """
            Args:
                node: 动态开点
                lc: left_cur
                rc: right_cur
                l: L, 左边界
                r: R, 右边界
                v: 更新的值

            Returns: None
        """
        if l <= lc and rc <= r:
            node.val = v
            # 注意产生变化懒标记就为True，因为更新有删除
            node.add = True
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)

    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> bool:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, True
        if l <= mid:
            ans = ans and SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = ans and SegmentTree.query(node.rs, mid + 1, rc, l, r)
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.val, node.rs.val = node.val, node.val
        # 注意产生变化懒标记就为True，因为更新有删除
        node.ls.add, node.rs.add = True, True
        node.add = False

    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为两者都true
        node.val = node.ls.val and node.rs.val


for _ in range(int(input())):
    n = int(input())
    arr = []
    ret = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        for x, y in arr:
            if (a <= x and y <= b) or (x <= a and b <= y):
                ret += 1
        arr.append((a, b))
    print(ret)
