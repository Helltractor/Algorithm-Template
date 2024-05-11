from typing import List


def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    ret, to_ret = 0, n + 1
    left, right = 0, 0

    for right in range(n):
        if ret < k:
            ret += nums[right]
        if ret >= k:
            to_ret = min(to_ret, right - left + 1)
        while ret > k:
            ret -= nums[left]
            left += 1
            if ret >= k:
                to_ret = min(to_ret, right - left + 1)
    return to_ret if to_ret <= n else -1


if __name__ == '__main__':
    nums = [17, 85, 93, -45, -21]
    print(shortestSubarray(nums, 150))
