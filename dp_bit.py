# _*_ coding: utf-8 _*_
# @File : dp_bit.py
# @Time : 2023/11/17 16:57
# @Author : Helltrackor


# 数位dp
# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/numbers-with-repeated-digits/solutions/1748539/by-endlesscheng-c5vg/
"""
    mask 表示前面选过的数字集合，换句话说，第 i 位要选的数字不能在 mask 中。

    isLimit 表示当前是否受到了 n 的约束（注意要构造的数字不能超过 n）。若为真，则第 i 位填入的数字至多为 s[i]，否则可以是 9。
    如果在受到约束的情况下填了 s[i]，那么后续填入的数字仍会受到 n 的约束。例如 n=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。

    isNum 表示 i 前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 1；若为真，则要填入的数字可以从 0 开始。
    例如 n=123，在 i=0 时跳过的话，相当于后面要构造的是一个 99 以内的数字了，如果 i=1 不跳过，那么相当于构造一个 10 到 99 的两位数，
    如果 i=1 跳过，相当于构造的是一个 9 以内的数字
"""


# @cache
# def dfs(i, mask, is_limit, is_num):
#     if i == len(s):
#         return is_num
#     ret = 0
#     if not is_num:
#         ret = dfs(i + 1, mask, False, False)
#     lo = 0 if is_num else 1
#     hi = int(s[i]) if is_limit else 9
#     for d in range(lo, hi + 1):
#         if (mask >> d & 1) == 0:
#             ret += dfs(i + 1, mask | (1 << d), is_limit and d == hi, True)
#     return ret

# link: https://leetcode.cn/problems/count-special-integers/
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache  # 记忆化搜索
        def f(i, mask, is_limit, is_num):
            if i == len(s):
                return int(is_num)  # is_num 为 True 表示得到了一个合法数字
            ret = 0
            if not is_num:  # 可以跳过当前数位
                ret = f(i + 1, mask, False, False)
            # low = 1 - int(is_num)
            low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if (mask >> d & 1) == 0:  # d 不在 mask 中
                    ret += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return ret

        return dfs(0, 0, True, False)


# 上下边界数位dp
# link: https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci/
"""
    limitHigh 表示当前是否受到了 finish 的约束（我们要构造的数字不能超过 finish。若为真，则第 iii 位填入的数字至多为 finish[i]，否则至多为 9，
    这个数记作 hi。如果在受到约束的情况下填了 finish[i，那么后续填入的数字仍会受到 finish 的约束。例如 finish=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。
    
    limitLow 表示当前是否受到了 start 的约束（我们要构造的数字不能低于 start。若为真，则第 i 位填入的数字至少为 start[i]，否则至少为 0，这个数记作 lo。
    如果在受到约束的情况下填了 start[i]，那么后续填入的数字仍会受到 start 的约束。
"""


# link: https://leetcode.cn/problems/count-the-number-of-powerful-integers/
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = '0' * (n - len(low)) + low  # 补前导零，和 high 对齐
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            res = 0
            if i < diff:  # 枚举这个数位填什么
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # 这个数位只能填 s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= min(hi, limit):
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res

        return dfs(0, True, True)


# link: https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/
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
