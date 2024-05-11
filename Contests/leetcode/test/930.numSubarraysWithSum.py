# from collections import defaultdict
import collections
from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    n = len(nums)
    # presum = [sum(nums[:i + 1]) for i in range(n)]
    hashmap = collections.defaultdict(int, {0: 1})
    ret = temp = 0
    for i in range(n):
        temp += nums[i]
        # temp = presum[i] - goal
        ret += hashmap[temp - goal]
        hashmap[temp] += 1
    return ret


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 1]
    print(numSubarraysWithSum(nums, 2))
