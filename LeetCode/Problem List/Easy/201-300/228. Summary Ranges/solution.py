class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        result = [str(nums[0])]
        first = str(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                result[-1] = first + '->' + str(nums[i])
            else:
                result.append(str(nums[i]))
                first = str(nums[i])
        return result
# nums = [0,1,2,4,5,7]
nums = [-2147483648,-2147483647,2147483647]
# nums = [-1,0,2,9]

test = Solution()
print(test.summaryRanges(nums=nums))