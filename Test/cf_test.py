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
    return


def solve_B():
    return


def solve_C():
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
