# https://leetcode.com/problems/single-number-iii/
from typing import Counter, List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap = Counter(nums)
        l = []
        for k, v in hashMap.items():
            if v == 1:
                l.append(k)

        return l
