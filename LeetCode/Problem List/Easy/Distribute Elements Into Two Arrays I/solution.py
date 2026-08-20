class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1: list = [nums[0]]
        arr2: list = [nums[1]]
        for index in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[index])
            else:
                arr2.append(nums[index])
        return arr1 + arr2