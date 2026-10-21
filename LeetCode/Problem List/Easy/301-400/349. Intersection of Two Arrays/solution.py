class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        result = []
        for char in nums1_set:
            if char in nums2_set:
                result.append(char)
        return result


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        result = []
        if len(nums1_set) < len(nums2_set):
            for char in nums1_set:
                if char in nums2_set:
                    result.append(char)
        elif len(nums1_set) > len(nums2_set):
            for char in nums2_set:
                if char in nums1_set:
                    result.append(char)
        else:
            for char in nums2_set:
                if char in nums1_set:
                    result.append(char)
        return result


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

test = Solution()
print(test.intersection(nums1, nums2))