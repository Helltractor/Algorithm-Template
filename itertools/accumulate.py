# _*_ coding: utf-8 _*_
# @File : accumulate.py
# @Time : 2024/5/3 14:53
# @Author : Helltractor

import operator

def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total

def list(iterable):
    'Return a list of the elements in the iterable or Convert the iterable to a list.'
    li = []
    it = iter(iterable)
    for i in it:
        li.append(i)
    return li

if __name__ == '__main__':
    a = list(accumulate(range(10), initial=0))
    # print(a.__iter__())
    print(a)
    for i in range(10):
        print(a[i])