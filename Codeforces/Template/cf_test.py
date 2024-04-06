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
    from collections import Counter, defaultdict, deque
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
        n, a, b = MII()
        if a * 2 > b:
            print(n % 2 * a + n // 2 * b)
        else:
            print(n * a)
    return


def solve_B():
    for _ in range(II()):
        n, c, d = MII()
        a = LII()
        a.sort()
        b = []
        for i in range(n):
            for j in range(n):
                b.append(a[0] + i * c + j * d)
        b.sort()
        if a == b:
            print("Yes")
        else:
            print("No")

    return


def solve_C():
    for _ in range(II()):
        n, k = MII()
        a = LII()
        q = deque(a)
        while k and q:
            if len(q) > 1:
                x = q.popleft()
                y = q.pop()
                if k >= min(x, y) * 2:
                    if x > y:
                        q.appendleft(x - y)
                    elif x < y:
                        q.append(y - x)
                    k -= min(x, y) * 2
                elif y >= x and k == 2 * min(x, y) - 1:
                    q.append(y - x + 1)
                    k -= 2 * min(x, y) - 1
                else:
                    q.appendleft(x)
                    q.append(y)
                    k = 0
            else:
                x = q.pop()
                if k < x:
                    q.append(x)
                    k = 0
        print(n - len(q))
    return


def solve_D():
    for _ in range(II()):
        n, m, k = MII()
        a = LII()
        b = LII()
        cnt = Counter(b)
        delta = 0
        for i in range(m):
            if a[i] in cnt:
                if cnt[a[i]] > 0:
                    delta += 1
                cnt[a[i]] -= 1
        ans = int(delta >= k)
        for i in range(m, n):
            if a[i - m] in cnt:
                if cnt[a[i - m]] >= 0:
                    delta -= 1
                cnt[a[i - m]] += 1
            if a[i] in cnt:
                if cnt[a[i]] > 0:
                    delta += 1
                cnt[a[i]] -= 1
            ans += int(delta >= k)
        print(ans)
    return



def solve_E():
    for _ in range(II()):
        n = II()
        s = I()

        for k in range(n, 0, -1):
            flag = True
            diff = [0] * (n + 1)
            cur = 0
            for i in range(n - k + 1):
                diff[i] += cur
                if diff[i] % 2 == int(s[i]):
                    diff[i] += 1
                    diff[i + k] -= 1
                cur = diff[i]
            for i in range(n - k + 1, n):
                diff[i] += diff[i - 1]
                if diff[i] % 2 == int(s[i]):
                    flag = False
                    break
            if flag:
                print(k)
                break
    return


def solve_F():
    for _ in range(II()):
        a, b, c, d = MII()
        ans = (a % 2) & (b % 2) & (c % 2)
        a //= 2
        b //= 2
        c //= 2
        d //= 2
        mn = min(b, c)
        print(ans + a + mn * 2 + (b + c - 2 * mn) + d)
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
    solve_B()
    # solve_C()
    # solve_D()
    # solve_E()
    # solve_F()
    # solve_G()