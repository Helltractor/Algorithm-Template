# _*_ coding: utf-8 _*_
# @File : cf_test.py
# @Time : 2024/1/14 23:05
# @Author : Helltractor

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
    from collections import Counter, defaultdict
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
        a, b, c = MII()
        if a < b < c:
            print("STAIR")
        elif a < b > c:
            print("PEAK")
        else:
            print("NONE")
    return


def solve_B():
    for _ in range(II()):
        n = II()
        m = 2 * n
        s = ''
        ss = ''
        for i in range(n):
            if i % 2:
                s += '..'
                ss += '##'
            else:
                s += '##'
                ss += '..'
        ans = []
        for i in range(n):
            if i % 2:
                ans.extend([ss, ss])
            else:
                ans.extend([s, s])
        for i in range(m):
            print(ans[i])

    return


def solve_C():
    for _ in range(II()):
        s = I()
        hh = s.split(':')
        a = int(hh[0])
        if a == 0:
            print(f"{str(12) + ':' + hh[1]} AM")
        elif a > 12:
            b = str(a - 12)
            print(f"{'0' * (2 - len(b)) + b + ':' + hh[1]} PM")
        elif a == 12:
            print(f"{s} PM")
        else:
            print(f"{s} AM")

    return


def solve_D():
    s = []
    for i in range(1, 64):
        s.append(int(bin(i)[2:]))
    vis = set(s)

    def dfs(x):
        if x > 10 ** 5:
            return
        vis.add(x)
        for i in s[1:]:
            dfs(x * i)
        return

    for i in s[1:]:
        dfs(i)
    for _ in range(II()):
        x = II()
        if x in vis:
            print("YES")
        else:
            print("NO")
    return


class StringHash:
    # 字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值
    def __init__(self, s):
        n = len(s)
        self.BASE = BASE = 131313  # 进制 31,131,13131,13331,131313
        self.MOD = MOD = 10 ** 13 + 7  # 10**13+37 ,10**13+51 ,10**13+99 ,10**13+129 ,10**13+183
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE + ord(s[i - 1])) % MOD

    # 用O(1)时间获取闭区间[l,r]（即s[l:r]）的哈希值，比切片要快
    def get(self, l, r):
        return (self.h[r + 1] - self.h[l] * self.p[r - l + 1]) % self.MOD


def solve_E():
    from collections import Counter
    for _ in range(II()):
        n = II()
        s = I()
        sh = StringHash(s)
        cnt = Counter(s)
        c = Counter()
        cc = Counter()
        ans = n
        for i in range(1, n // 2 + 1):
            c[s[i - 1]] += 1
            cc[s[n - i]] += 1
            if n % i == 0:
                m = n // i
                ss = 0
                sss = 0
                for j in range(m):
                    if sh.get(j * i, (j + 1) * i - 1) != sh.get(0, i - 1):
                        if ss:
                            ss = -1
                        else:
                            tmp = 0
                            for x, y in zip(s[j * i: (j + i) * i], s[: i]):
                                if x != y:
                                    tmp += 1
                            if tmp == 1:
                                ss = 1
                            else:
                                ss = -1
                    if sh.get(j * i, (j + 1) * i - 1) != sh.get(n - i, n - 1):
                        if sss:
                            sss = -1
                        else:
                            tmp = 0
                            for x, y in zip(s[j * i: (j + i) * i], s[n - i:]):
                                if x != y:
                                    tmp += 1
                            if tmp == 1:
                                sss = 1
                            else:
                                sss = -1
            if ss >= 0 or sss >= 0:
                ans = min(ans, i)
                break
        print(ans)
    return


def solve_F():
    for _ in range(II()):
        a, b, c = MII()

        if a:
            n = len(bin(a)) - 3
            a -= (1 << n) - 1
            ans = n + (a > 0)
            if b + c < (1 << n) + a or c != (1 << n) + a:
                print(-1)
            else:
                from math import ceil
                ans += ceil((b - (1 << n) + a) / ((1 << n) + a))
                print(ans)
        else:
            if c != 1:
                print(-1)
            else:
                print(b)
    return


def solve_G():
    for _ in range(II()):
        n = II()
        a = defaultdict(Counter)
        b = []
        c = []
    return


if __name__ == "__main__":
    # solve_A()
    # solve_B()
    # solve_C()
    # solve_D()
    # solve_E()
    solve_F()
    # solve_G()
