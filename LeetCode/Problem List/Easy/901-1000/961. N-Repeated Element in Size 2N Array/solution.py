class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        map_nums = {}
        for num in nums:
            map_nums[num] = map_nums.get(num, 0) + 1
        map_nums_desc = dict(
            sorted(map_nums.items(), key=lambda item: item[1], reverse=True)
        )
        return next(iter(map_nums_desc))