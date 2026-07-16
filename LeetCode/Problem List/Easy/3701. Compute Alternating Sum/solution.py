class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        total: int = 0
        for index, num in enumerate(nums):
            if index % 2 != 0:
                total -= num
            else:
                total += num
        return total


nums = [1,3,5,7]

test_solution = Solution()
print(test_solution.alternatingSum(nums))
