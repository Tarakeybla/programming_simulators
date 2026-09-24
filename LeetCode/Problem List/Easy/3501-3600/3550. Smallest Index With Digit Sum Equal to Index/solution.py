class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, value in enumerate(nums):
            # if sum([int(digit) for digit in str(value)]) == index:
            #     return index
            if sum(map(int, str(value))) == index:
                return index
        return -1