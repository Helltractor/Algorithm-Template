# _*_ coding: utf-8 _*_
# @File : example2.py
# @Time : 2024/4/21 19:59
# @Author : Helltractor

from functools import cache

# @Author : 灵茶山艾府
# @link : https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low, high = str(low), str(high)
        n = len(high)
        diff = n - len(low)
        low = '0' * diff + low

        @cache
        def dfs(i: int, cnt: int, mod: int, limit_low: bool, limit_high: bool, is_num: bool) -> int:
            if i == n:
                return cnt == mod == 0
            res = 0

            if i < diff and not is_num:  # 可以跳过当前数位
                res += dfs(i + 1, 0, 0, True, False, False)

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            for d in range(max(lo, 1 - is_num), hi + 1):  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                res += dfs(i + 1, cnt + 1 - (d & 1) * 2, (mod * 10 + d) % k,
                           limit_low and d == lo, limit_high and d == hi, True)
            return res

        return dfs(0, 0, 0, True, True, False)