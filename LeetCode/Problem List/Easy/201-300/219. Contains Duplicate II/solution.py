class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        DIGIT_MAP = {}
        for index, value in enumerate(nums):
            if value not in DIGIT_MAP:
                DIGIT_MAP[value] = {
                    'index': [index],
                    'count': 1
                }
            else:
                DIGIT_MAP[value]['index'].append(index)
                DIGIT_MAP[value]['count'] += 1
        for item in DIGIT_MAP.items():
            if item[1]['count'] >= 2:
                indexs = item[1]['index']
                for i in range(len(indexs) - 1):
                    for j in range (i + 1, len(indexs)):
                        if abs(indexs[i] - indexs[j]) <= k:
                            return True
                        break
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        LAST_INDEX_MAP = dict()
        for index, value in enumerate(nums):
            if value in LAST_INDEX_MAP:
                if index - LAST_INDEX_MAP[value] <= k:
                    return True
            LAST_INDEX_MAP[value] = index
        return False


nums = [1,0,1,1]
k = 1

test = Solution()
print(test.containsNearbyDuplicate(nums, k))


# Варианты формирования словаря:
            # if value not in DIGIT_MAP:
            #     DIGIT_MAP[value] = [index]
            # else:
            #     DIGIT_MAP[value].append(index)

            # DIGIT_MAP.setdefault(value, []).append(index)
