from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    if not n or nums[-1] < target or nums[0] > target: return [-1, -1]
    if n == 1 and nums[0] == target: return [0, 0]
    # if nums[0] == target == nums[-1]: return [0, n - 1]
    left, right = 0, n - 1
    while left <= right:
        mid = left + right + 1 >> 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if nums[left] == target:
        for i in range(left, n):
            if nums[i] != nums[left]:
                break
            right += 1
        return [left, right]
    return [-1, -1]


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 8, 9, 71]
    nums1 = [1, 4]
    nums2 = [2, 2]
    print(searchRange(nums2, 2))
