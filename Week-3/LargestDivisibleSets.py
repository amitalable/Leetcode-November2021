# https://leetcode.com/problems/largest-divisible-subset

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        # contains sets starting with that number
        res = [[num] for num in nums]

        for i in range(n):
            for j in range(i):
                # to ensure the length of the set is maximal
                if (nums[i] % nums[j]) == 0 and len(res[i]) < len(res[j]) + 1:
                    res[i] = res[j] + [nums[i]]

        return max(res, key=len)  # return max length set
