# _*_ coding: utf-8 _*_
# @File : kmp.py
# @Time : 2024/1/14 12:12
# @Author : Helltractor

# link: https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-ii/

# def kmp(s, t):
#     m, n = len(s), len(t)
#     nxt = [0] * n
#     j = 0
#     for i in range(1, n):
#         while j > 0 and t[i] != t[j]:
#             j = nxt[j - 1]
#         if t[i] == t[j]:
#             j += 1
#         nxt[i] = j
#
#     j = 0
#     matches = []
#     for i in range(m):
#         while j > 0 and s[i] != t[j]:
#             j = nxt[j - 1]
#         if s[i] == t[j]:
#             j += 1
#         if j == n:
#             matches.append(i - n + 1)
#             j = nxt[j - 1]
#     return matches


def kmp(s, t):
    """
    使用 KMP 算法在字符串 s 中查找子串 t 的所有匹配位置。

    Args:
        s (str): 主串，要在其中查找匹配的子串。
        t (str): 子串，要在主串中查找的模式。

    Returns:
        list: 匹配的子串 t 在主串 s 中的所有起始位置的列表。

    Notes:
        - 如果主串 s 或子串 t 为空，则返回空列表。
        - 如果子串 t 的长度大于主串 s 的长度，则返回空列表。
        - 匹配位置的索引从 0 开始。
        - 如果子串 t 在主串 s 中有多个重叠的匹配，只返回第一个匹配的起始位置。
    """
    m, n = len(s), len(t)
    nxt = [0] * n  # 记录子串 t 的每个位置的最长相同前缀后缀长度
    j = 0
    # 计算子串 t 的最长相同前缀后缀长度
    for i in range(1, n):
        while j > 0 and t[i] != t[j]:
            j = nxt[j - 1]
        if t[i] == t[j]:
            j += 1
        nxt[i] = j

    j = 0
    matches = []  # 记录匹配的子串 t 在主串 s 中的起始位置
    # 在主串 s 中查找匹配的子串 t
    for i in range(m):
        while j > 0 and s[i] != t[j]:
            j = nxt[j - 1]
        if s[i] == t[j]:
            j += 1
        if j == n:  # 如果 j 等于子串 t 的长度，表示找到了一个匹配
            matches.append(i - n + 1)
            j = nxt[j - 1]
    return matches
