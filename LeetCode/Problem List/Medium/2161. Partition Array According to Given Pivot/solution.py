class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        max_nums, pivot_nums, min_nums = list(), list(), list()
        for num in nums:
            if num > pivot:
                max_nums.append(num)
            elif num == pivot:
                pivot_nums.append(num)
            else:
                min_nums.append(num)
        return min_nums + pivot_nums + max_nums
    

nums = [9,12,5,10,14,3,10]
pivot = 10

test_solution = Solution()
print(test_solution.pivotArray(nums, pivot))
