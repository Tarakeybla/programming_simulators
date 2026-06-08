# This solution is questionable because it changes the input list (.extend()).

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums
    
test_solution = Solution()

print(test_solution.getConcatenation([1, 2, 3]))


# I like this solution better because it doesn't modify the input list.

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2
