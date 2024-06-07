from typing import List


def longestSubarray(nums: List[int]) -> int:
    n = len(nums)
    if n == sum(nums): return n - 1
    for i in range(n, 0, -1):
        for j in range(n - i + 1):
            if i - 1 == sum(nums[j: j + i]): return i - 1
    return 0


if __name__ == '__main__':
    nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
    print(longestSubarray(nums))
