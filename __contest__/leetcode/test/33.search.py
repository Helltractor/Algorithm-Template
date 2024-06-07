from typing import List


def search(nums: List[int], target: int) -> int:
    if not nums: return -1
    if len(nums) == 1: return 0 if nums[0] == target else -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + right + 1 >> 1
        if nums[mid] >= nums[0]:
            left = mid
        else:
            right = mid - 1
    print(left)
    if nums[0] > target:
        left = left + 1
        right = len(nums) - 1
    else:
        left = 0
    while left < right:
        mid = left + right >> 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right if nums[right] == target else -1


if __name__ == '__main__':
    nums = [1, 3]
    print(search(nums, 3))
