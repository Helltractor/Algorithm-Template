# _*_ coding: utf-8 _*_
# @File : my_cache.py
# @Time : 2024/5/8 16:36
# @Author : Helltractor

def my_cache(func):
    cache = {}

    def wrapper(*args):
        key = args
        if key in cache:
            return cache[key]
        result = func(*args)
        cache[key] = result
        return result

    return wrapper