from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n >= 1:
            value_in_nums2 = nums2.pop(0)
            for index, value in enumerate(nums1):
                if value_in_nums2 <= value:
                    nums1.insert(index, value_in_nums2)
                    del nums1[-1]
                    n -= 1
                    m += 1
                    break
                elif index == m:
                    nums1.insert(index, value_in_nums2)
                    del nums1[-1]
                    n -= 1
                    m += 1
                    break


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

test = Solution()
print(test.merge(nums1=nums1, m=m, nums2=nums2, n=n))