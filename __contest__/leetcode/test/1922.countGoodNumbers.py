class Solution:
    # 快速幂 -> pow函数
    """
        def quick_mul(x: int, y: int, z: int)-> int:
            ret = 1
            while y:
                if y % 2 == 1:
                    ret = ret * x % z
                x = x * x % z
                y //= 2
            return ret
    """
    """
        def quick_mul(n: int, x: int):
            if n == 0:
                return 1.0
            y = quick_mul(n//2)
            return y * y if n % 2 == 0 else y * y * x
    """
    """
        def quick_mul(n: int, x: int):
            ret = 1.0
            x_pow = x
            while n > 0:
                if n % 2:
                    ret *= x_pow
                x_pow *= x_pow
                n //= 2
            return ret
    """

    def countGoodNumbers(n: int) -> int:
        MOD = 10 ** 9 + 7

        def quick_mul(x: int, y: int, z: int) -> int:
            ret = 1
            while y:
                if y % 2 == 1:
                    ret = ret * x % z
                x = x * x % z
                y //= 2
            return ret

        x = quick_mul(5, (n + 1) // 2, MOD)
        y = quick_mul(4, n // 2, MOD)
        return x * y % MOD

    # pow函数
    def countGoodNumbers1(n: int) -> int:
        MOD = 10 ** 9 + 7
        return pow(4, n // 2, MOD) * pow(5, (n + 1) // 2, MOD) % MOD


if __name__ == '__main__':
    print(Solution.countGoodNumbers1(99999999))
