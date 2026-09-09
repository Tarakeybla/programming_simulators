class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        digit_map = {}
        for num in nums:
            digit_map[num] = digit_map.get(num, 0) + 1
        result = []
        for key, value in digit_map.items():
            if value == 2:
                result.append(key)
        return result
        # return list(
        #     dict(
        #         sorted(
        #             digit_map.items(),
        #             key=lambda item: item[1],
        #             reverse=True
        #         )
        #     ).keys()
        # )[:2]


nums = [7,1,5,4,3,4,6,0,9,5,8,2]

test = Solution()
print(test.getSneakyNumbers(nums))
