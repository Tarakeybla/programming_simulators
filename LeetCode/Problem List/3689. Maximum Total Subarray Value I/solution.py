# This solution is very simple, but the description of this exercise is very complex...
# Medium....

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        return (max(nums) - min(nums)) * k

test_solution = Solution()

print(test_solution.maxTotalValue([4,2,5,1], 3))

# If the same subarray can be used multiple times, it is enough
# to find the subarray with the maximum value and multiply it by k.
