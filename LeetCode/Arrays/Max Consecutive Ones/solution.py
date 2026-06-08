# This is my solution, where I used the resulting list to store
# the lengths of all consecutive sequences of ones in the input list.
#
# After the loop finishes, the counter value is also added to the list
# to preserve the length of the last sequence.
#
# To eliminate duplicates, the list is converted into a set.
#
# The maximum sequence length is then determined using the max() function.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count: int = 0
        result: list[int] = []
        for num in nums:
            if num == 1:
                count += 1
            elif num == 0:
                result.append(count)
                count = 0
        result.append(count)       
        return max(set(result))
    
test_solution = Solution()

print(test_solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
