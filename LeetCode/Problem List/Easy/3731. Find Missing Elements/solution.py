from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result: list = []
        for num in range(min(nums), max(nums)):
            if num not in nums:
                result.append(num)
        return result
