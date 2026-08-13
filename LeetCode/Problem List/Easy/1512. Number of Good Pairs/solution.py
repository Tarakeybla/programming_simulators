from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count: int = 0
        for start_point in range(len(nums)):
            for end_point in range(start_point + 1, len(nums)):
                if nums[start_point] == nums[end_point]:
                    count += 1
        return count

nums = [1,2,3,1,1,3]

test_solution = Solution()
print(test_solution.numIdenticalPairs(nums=nums))
