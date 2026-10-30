class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set(nums)
        result = []
        for num in range(1, len(nums) + 1):
            if num not in seen:
                result.append(num)
        return result