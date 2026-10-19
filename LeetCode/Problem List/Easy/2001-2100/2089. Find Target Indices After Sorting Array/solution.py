class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []
        index = 0
        for value in nums:
            if target == value:
                result.append(index)
            index += 1
        return result