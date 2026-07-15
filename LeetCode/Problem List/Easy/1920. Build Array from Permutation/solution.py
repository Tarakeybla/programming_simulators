class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        result_array: list = []
        for position in range(len(nums)):
            result_array.append(nums[nums[position]])
        return result_array  


nums = [0,2,1,5,3,4]

test_solution = Solution()
print(test_solution.buildArray(nums))


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[position]] for position in range(len(nums))]
