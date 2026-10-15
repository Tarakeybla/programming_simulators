class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        result = 0
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                result += len((set(nums[start:end])))**2
        return result