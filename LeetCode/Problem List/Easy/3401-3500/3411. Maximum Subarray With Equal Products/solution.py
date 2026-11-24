from typing import List
from math import gcd, lcm, prod

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result = 0
        for start_point in range(len(nums)):
            for end_point in range(start_point + 1, len(nums) + 1):
                current_arr = nums[start_point:end_point]
                if (prod(current_arr) == lcm(*current_arr) * gcd(*current_arr) 
                    and len(current_arr) >= result):
                    result = len(current_arr)
        return result


nums = [1,2,1,2,1,1,1]

test = Solution()
print(test.maxLength(nums))