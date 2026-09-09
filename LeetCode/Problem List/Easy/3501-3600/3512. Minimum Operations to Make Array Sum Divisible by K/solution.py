class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return self.sum(nums) % k

    def sum(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            total += num
        return total
    

nums = [3,9,7]

test_solutions = Solution()
print(test_solutions.minOperations(nums, 5))
