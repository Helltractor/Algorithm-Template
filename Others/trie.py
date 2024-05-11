# _*_ coding: utf-8 _*_
# @File : trie.py
# @Time : 2023/12/10 21:42
# @Author : Helltractor
from collections import defaultdict


class Node:
    __slots__ = 'son', 'is_end'

    def __init__(self):
        # self.son = dict()
        self.son = defaultdict(Node)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root  # 从根节点开始插入单词的字符
        for char in word:
            cur = cur.son[char]  # 移动到下一个节点
        cur.is_end = True  # 标记最后一个节点为单词的结尾

    def search(self, word: str) -> bool:
        cur = self.root  # 从根节点开始搜索单词
        for char in word:
            cur = cur.son.get(char)
            if cur is None:  # 如果字符不存在，单词不存在
                return False
            cur = cur.son[char]  # 移动到下一个节点
        return cur.is_end  # 返回最后一个节点是否标记为单词的结尾

    def startsWith(self, prefix: str) -> bool:  # 检查是否存在以给定前缀开头的单词
        cur = self.root
        for c in prefix:
            cur = cur.son.get(c)
            if cur is None:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.children = {}  # 存储子节点的字典，键是字符，值是TrieNode
        self.is_end_of_word = False  # 标记当前节点是否是一个单词的结尾


class Trie:
    def __init__(self):
        self.root = TrieNode()  # 创建根节点

    def insert(self, word: str) -> None:
        node = self.root  # 从根节点开始插入单词的字符
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # 如果字符不存在，创建一个新节点
            node = node.children[char]  # 移动到下一个节点
        node.is_end_of_word = True  # 标记最后一个节点为单词的结尾

    def search(self, word: str) -> bool:
        node = self.root  # 从根节点开始搜索单词
        for char in word:
            if char not in node.children:
                return False  # 如果字符不存在，单词不存在
            node = node.children[char]  # 移动到下一个节点
        return node.is_end_of_word  # 返回最后一个节点是否标记为单词的结尾

    def starts_with(self, prefix: str) -> bool:  # 检查是否存在以给定前缀开头的单词
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str):
        def _delete(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    return not bool(node.children)  # 如果没有子节点，可以删除该节点
                return False

            char = word[index]
            if char not in node.children:
                return False

            should_delete = _delete(node.children[char], word, index + 1)

            if should_delete:
                del node.children[char]
                return not bool(node.children)
            return False

        _delete(self.root, word, 0)


if __name__ == '__main__':

    trie = lambda: defaultdict(trie)  # 嵌套defaultdict
    root = trie()

    words = ['']
    for word in words:
        cur = root  # 从根节点开始插入单词的字符
        for c in word:
            cur = cur[c]  # 移动到下一个节点
        cur[None] = True  # 标记最后一个节点为单词的结尾

    word = ''
    cur = root  # 从根节点开始插入单词的字符
    for c in word:
        cur = cur[c]  # 移动到下一个节点
    cur[None] = True  # 标记最后一个节点为单词的结尾
