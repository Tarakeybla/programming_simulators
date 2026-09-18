class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False