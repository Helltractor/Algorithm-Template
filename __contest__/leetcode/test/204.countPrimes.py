class Solution:

    def Primes(n):
        primes = []
        for i in range(2, n):
            if all(i % j != 0 for j in range(2, i)):
                primes.append(i)
        return primes

    # 枚举
    def countPrimes1(n: int) -> int:
        def isPrime(n):
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True if n > 1 else False

        ret = 0
        for i in range(2, n):
            if isPrime(i):
                ret += 1
        return ret

    # 枚举优化
    def countPrimes2(n: int) -> int:
        def isPrime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True if n > 1 else False

        ret = 0
        for i in range(2, n):
            if isPrime(i):
                ret += 1
        return ret

    # 埃氏筛
    """
        primes = []
        is_prime = [True] * n
        # is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
                for j in range(i ** 2, n, i):
                    is_prime[j] = False
        # 防止下标越界
        primes.extend([n, n])
    """

    def countPrimes3(n: int) -> int:
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
                for j in range(i ** 2, n, i):
                    is_prime[j] = False
        return len(primes)

    # 线性筛
    """
        primes = []
        is_prime = [True] * n
        # is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n: break
                is_prime[i * p] = False
                if i % p == 0: break
        # 防止下标越界
        primes.extend([n, n])
    """

    def countPrimes4(n: int) -> int:
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        return len(primes)


if __name__ == '__main__':
    print("---给定整数n，返回所有小于非负整数n的质数的数量---")
    n = input('输入整数n：')
    print(Solution.countPrimes1(int(n)))
    print(Solution.countPrimes2(int(n)))
    print(Solution.countPrimes3(int(n)))
    print(Solution.countPrimes4(int(n)))
