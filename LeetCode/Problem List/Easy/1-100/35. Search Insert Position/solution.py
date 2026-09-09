# This solution uses binary search.
# We repeatedly divide the search range in half and determine
# which half may contain the target value.
# Based on this, we move either the left or right boundary,
# gradually narrowing the search area.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


test_solution = Solution()

# nums = [1, 3, 5, 6]
# target = 7
nums = [1, 2, 3, 4, 6, 8, 9]
target = 10

print(test_solution.searchInsert(nums, target))
