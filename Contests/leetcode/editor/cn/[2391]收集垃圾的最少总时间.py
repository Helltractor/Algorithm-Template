# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ret = 0
        tmp = {}
        pre = 0
        for g, t in zip(garbage, [0] + travel):
            ret += len(g)
            pre += t
            for c in g:
                tmp[c] = pre
        return ret + sum(tmp.values())
# leetcode submit region end(Prohibit modification and deletion)