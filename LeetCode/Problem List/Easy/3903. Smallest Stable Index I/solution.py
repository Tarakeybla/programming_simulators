class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if max(nums[:i+1]) - min(nums[i:]) <= k:
                return i
        return -1

nums = [5,0,1,4]
k = 3

test = Solution()
print(test.firstStableIndex(nums=nums, k=k))