from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            if nums[index] % 2 == 0:
                nums[index] = 0
            else:
                nums[index] = 1
            print(nums)
        nums.sort()
        return nums


nums = [4,3,2,1]

test_solution = Solution()
print(test_solution.transformArray(nums))
