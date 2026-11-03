class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = 0
        maxx = max(nums)
        for num in nums:
            if num < maxx:
                total += maxx - num
        return total


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)