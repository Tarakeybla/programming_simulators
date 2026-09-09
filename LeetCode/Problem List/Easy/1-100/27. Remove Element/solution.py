# This is a solution is not optimal, but it is simple and easy to understand.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

test_solution = Solution()
print(test_solution.removeElement([3, 2, 2, 3], 3))

# This is an optimal solution because it uses a single pass over the input list
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k
