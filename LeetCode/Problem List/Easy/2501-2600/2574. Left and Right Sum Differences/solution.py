class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = [0]
        right_sum = [0]
        len_nums = len(nums) - 1
        for i in range(len_nums):
            left_sum.append(left_sum[-1] + nums[i])
        for i in range(len_nums - 1, -1, -1):
            right_sum.insert(0, (right_sum[0] + nums[i + 1]))
        return [abs(left_sum[i] - right_sum[i]) for i in range(len_nums + 1)]

nums = [10,4,8,3]

test = Solution()
print(test.leftRightDifference(nums))
