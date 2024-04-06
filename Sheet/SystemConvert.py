# _*_ coding: utf-8 _*_
# @File : SystemConvert.py
# @Time : 2024/4/6 21:04
# @Author : Helltractor

class SystemConvert:
    """
    TODO: 随机位数开始计算第 n 位 m 进制数
    """

    """
    TODO: n 进制转换为 m 进制
    """

    # 十进制转换为 m 进制
    @staticmethod
    def convert(x: int, m: int) -> str:
        y = ''
        while x:
            y += str(x % m)
            x //= m
        return y[::-1]

    # 从 1 开始计算处于上第 n 位 m 进制数
    @staticmethod
    def calculate_count(n: int, m: int) -> tuple:
        base = m - 1
        count = 0
        length = 1
        while n:
            tmp = base * length
            if n > tmp:
                length += 1
                base *= m
                count += tmp
            else:
                div, mod = divmod(n, length)
                count += div + (mod > 0)
                mod = (mod + length - 1) % length

                # ans = self.convert(count, m)
                # print(ans[mod])

                # 第 count 个 m 进制数，余 mod 位
                return count, mod
            n -= tmp
        return 0, 0


if __name__ == '__main__':
    sh = SystemConvert()
    print(sh.calculate_count(10, 10))