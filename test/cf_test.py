# _*_ coding: utf-8 _*_
# @File : cf_test.py
# @Time : 2024/1/14 23:05
# @Author : Helltractor
from types import GeneratorType

ImportType = 1
InputType = 1
ConstType = 1
if ImportType:
    import sys, random
    # sys.exit() 退出程序
    # sys.setrecursionlimit(10**6) #调整栈空间
    # randint(a,b)从[a,b]范围随机选择一个数
    # choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
    # shuffle(x)将一个可变的序列x中的元素打乱
    # reduce(op,迭代对象)
    # bisect_left(x) 大于等于x的第一个下标
    # bisect_right(x) 大于x的第一个下标
    # accumulate(a)用a序列生成一个累积迭代器，一般list化前面放个[0]做前缀和用
    # combinations(a,k)a序列选k个 组合迭代器
    # permutations(a,k)a序列选k个 排列迭代器
    # heapify将列表转为堆
    # 小写字母，大写字母，十进制数字
    # ceil向上取整，floor向下取整 ，sqrt开方 ，factorial阶乘
    # Decimal(s) 实例化Decimal对象,一般使用字符串
    # getcontext().prec=100 修改精度

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")


    def I():
        return input()


    def II():
        return int(input())


    def MII():
        return map(int, input().split())


    def LI():
        return list(input().split())


    def LII():
        return list(map(int, input().split()))


    def GMI():
        return map(lambda x: int(x) - 1, input().split())


    def LGMI():
        return list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353


def main():
    return


def solve_A():
    for _ in range(II()):
        n = II()
        q = LII()
        p = sorted(q)
        ans = 0
        mid = p[(n + 1) // 2 - 1]
        for i in range((n + 1) // 2 - 1, n):
            if p[i] <= mid:
                ans += mid - p[i] + 1
        print(ans)
    return


def solve_B():
    for _ in range(II()):
        n, k = MII()
        a = LII()
        MOD = 10 ** 9 + 7
        cur = (1 << k) - 1
        s = 0
        ans = 0
        cnt = 0
        for i, x in enumerate(a):
            s += x
            if cnt + x > 0:
                cnt += x
            else:
                cnt = 0
            ans = max(ans, cnt)
        print((ans * cur + s + MOD) % MOD)
    return


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def solve_C():
    for _ in range(II()):
        n, k = MII()
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = MII()
            g[u].append(v)
            g[v].append(u)

        def check(m):
            ans = 0

            @bootstrap
            def dfs(x, fa):
                nonlocal ans
                c = 1
                for y in g[x]:
                    if y == fa:
                        continue
                    c += yield (dfs(y, x))
                if c >= m:
                    ans += 1
                    c = 0
                yield c

            cc = dfs(1, 0)
            if cc < m:
                ans -= 1
            return ans >= k

        l = 1
        r = n
        while l <= r:
            m = l + r >> 1
            if check(m):
                l = m + 1
            else:
                r = m - 1
        print(r)
    return


def solve_D():
    return


def solve_E():
    return


if __name__ == "__main__":
    # solve_A()
    # solve_B()
    solve_C()
    # solve_D()
    # solve_E()
