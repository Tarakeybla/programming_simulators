from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = []
        max_first = max(nums)
        result.append(nums.pop(nums.index(max_first)))
        max_second = max(nums)
        result.append(nums.pop(nums.index(max_second)))
        return (result[0] - 1) * (result[1] - 1)


nums = [3,4,5,2]

test_solution = Solution()
print(test_solution.maxProduct(nums))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
