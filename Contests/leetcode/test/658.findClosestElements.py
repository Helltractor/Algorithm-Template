from typing import List


# False
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    n = len(arr)
    cur = 0
    for _ in range(n):
        if cur < n - k and abs(arr[cur] - x) > abs(arr[cur + k] - x):
            cur += 1
        # print(cur)
    return arr[cur: cur + k]


# 二分，滑动窗口
def findClosestElements1(arr: List[int], k: int, x: int) -> List[int]:
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        mid = right + left + 1 >> 1
        if mid + k < n and x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid - 1
    return arr[left: left + k]


# 二分，滑动窗口
def findClosestElements2(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left <= right:
        mid = right + left >> 1
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid - 1
    return arr[left: left + k]


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 2, 2, 2, 3, 3, 100]
    arr1 = [1, 1, 1, 10, 10, 10]
    print(findClosestElements1(arr, 3, 3))
    print(findClosestElements(arr1, 1, 10))
