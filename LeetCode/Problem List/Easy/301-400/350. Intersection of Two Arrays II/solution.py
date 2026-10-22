from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        NUMS1_MAP = Counter(nums1)
        NUMS2_MAP = Counter(nums2)
        result = []

        if len(NUMS1_MAP) < len(NUMS2_MAP):
            for key, value in NUMS1_MAP.items():
                if key in NUMS2_MAP:
                    if value == NUMS2_MAP[key]:
                        for _ in range(value):
                            result.append(key)
                    else:
                        for _ in range(min(value, NUMS2_MAP[key])):
                            result.append(key)
        elif len(NUMS1_MAP) > len(NUMS2_MAP):
            for key, value in NUMS2_MAP.items():
                if key in NUMS1_MAP:
                    if value == NUMS1_MAP[key]:
                        for _ in range(value):
                            result.append(key)
                    else:
                        for _ in range(min(value, NUMS1_MAP[key])):
                            result.append(key)
        else:
            for key, value in NUMS2_MAP.items():
                if key in NUMS1_MAP:
                    if value == NUMS1_MAP[key]:
                        for _ in range(value):
                            result.append(key)
                    else:
                        for _ in range(min(value, NUMS1_MAP[key])):
                            result.append(key)
        return result

nums1 = [1,2,2,1]
nums2 = [2,2]

test = Solution()
print(test.intersect(nums1, nums2))
        
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        count = Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num]-=1

        return res
        