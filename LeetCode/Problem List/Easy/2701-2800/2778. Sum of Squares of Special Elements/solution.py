from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        for index in range(1, len(nums) + 1):
            if len(nums) % index == 0:
                result += nums[index - 1]**2
        return result