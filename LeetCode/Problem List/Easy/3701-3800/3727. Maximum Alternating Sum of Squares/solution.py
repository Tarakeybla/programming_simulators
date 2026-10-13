class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = self.clear_arr(nums=nums)
        score = 0
        while len(nums) >= 2:
            score += nums.pop(-1) ** 2 - nums.pop(0) ** 2
        if len(nums) != 0:
            score += nums[-1] ** 2
        return score

    def clear_arr(self, nums: list[int]) -> list[int]:
        nums = [abs(num) for num in nums]
        nums.sort()
        return nums