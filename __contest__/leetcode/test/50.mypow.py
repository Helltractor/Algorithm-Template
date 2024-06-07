class Solution:
    # 快速幂 -> pow函数
    def quick_mul(x: int, y: int, z: int) -> int:
        ret = 1
        while y:
            if y % 2:
                ret = ret * x % z
            x = x * x % z
            y //= 2
        return ret

    def quick_mul1(n: int, x: int):
        if n == 0:
            return 1.0
        y = Solution.quick_mul1(n // 2, x)
        return y * y if n % 2 == 0 else y * y * x

    def quick_mul2(n: int, x: int):
        ret = 1.0
        x_pow = x
        while n > 0:
            if n % 2:
                ret *= x_pow
            x_pow *= x_pow
            n //= 2
        return ret

    def myPow(x: float, n: int) -> float:
        return Solution.quick_mul2(x, n) if n >= 0 else 1.0 / Solution.quick_mul2(x, -n)


if __name__ == '__main__':
    print(Solution.myPow(5.0, 5))
