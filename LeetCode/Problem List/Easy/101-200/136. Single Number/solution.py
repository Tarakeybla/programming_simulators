from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        return [key for key, value in count.items() if value == 1][0]

nums = [2,2,1]

test = Solution()
print(test.singleNumber(nums))

#XOR - вспомнить про него (взаимное уничтожение пар)