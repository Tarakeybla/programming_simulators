# This solution uses a loop to iterate over two parts of the array.
# The first part starts with element i and the second with element i+n.
# Both elements are added to the resulting list to shuffle the array.

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result: list[int] = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

test_solution = Solution()

print(test_solution.shuffle([2, 5, 1, 3, 4, 7], 3))
