from typing import List


# 脑筋急转弯
def findValueOfPartition(nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    print(nums)
    min_ = nums[n - 1] - nums[0]
    if n == 2: return min_
    left, right = 0, n - 1
    while left < right:
        if nums[right] == nums[right - 1] or nums[left] == nums[left + 1]:
            return 0
        if nums[right] == nums[right - 1] + 1 or nums[left] == nums[left + 1] - 1:
            return 1
        if nums[right] - nums[left + 1] < nums[right - 1] - nums[left]:
            left += 1
        elif nums[right] - nums[left + 1] > nums[right - 1] - nums[left]:
            right -= 1
        else:
            # if nums[right] - nums[left] == right - left and (right - left) % 2 == 0:
            # left += 1
            left += 1
            right -= 1
        min_ = min(min_, abs(nums[right] - nums[left]))
        print(min_)
    return min_


if __name__ == '__main__':
    num = [54, 75, 6, 20, 49, 94, 97, 20, 97]
    num1 = [87, 3, 46, 5, 14, 4]
    num2 = [10, 59, 66, 61, 11, 89, 3, 58, 87]
    print(findValueOfPartition(num1))
