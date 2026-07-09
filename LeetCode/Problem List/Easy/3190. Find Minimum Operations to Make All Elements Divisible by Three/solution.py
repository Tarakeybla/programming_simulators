class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        divider: int = 3
        count: int = 0
        for dividend in nums:
            if dividend % divider != 0:
                count += 1
        return count

nums = [1,2,3,4]

test_solution = Solution()
print(test_solution.minimumOperations(nums))
