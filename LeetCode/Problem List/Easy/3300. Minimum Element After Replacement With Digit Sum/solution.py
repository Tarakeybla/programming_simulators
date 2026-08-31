from sys import maxsize
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        minn = maxsize
        for num in nums:
            result = sum([int(digit) for digit in str(num)])
            if minn > result:
                minn = result
        return minn

nums = [10,12,13,14]

test = Solution()
print(test.minElement(nums))
