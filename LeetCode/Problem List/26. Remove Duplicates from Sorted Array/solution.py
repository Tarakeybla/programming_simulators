# Two solutions were devised.
# The key point is to change the input array.

# The first solution used the set() metod to get unique values in the array and override it.
# But this solution is wrong :(

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


# The second solution used the loop to reorder the values in the array and count the unique values
# The k equel 1 becouse the minimal length of an array in 1, and the first value in an array is always unique.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k

nums = [0,0,1,1,1,2,2,3,3,4]

test_solution = Solution()
print(test_solution.removeDuplicates(nums))