from collections import Counter 


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return list(
            (dict(sorted(
                (Counter(nums)).items(),
                key=lambda item: item[1],
                reverse=True)
            )).keys()
        )[0]

nums = [3,3,4]

test = Solution()
print(test.majorityElement(nums))