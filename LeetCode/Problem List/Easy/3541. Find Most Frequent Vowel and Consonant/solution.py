class Solution:
    def maxFreqSum(self, s: str) -> int:
        vovel_map: dict = {}
        consonant_map: dict = {}
        for char in s:
            if char not in 'aeiou':
                consonant_map[char] = consonant_map.get(char, 0) + 1
            else:
                vovel_map[char] = vovel_map.get(char, 0) + 1
        vovel_result = max(vovel_map.values(), default=0)
        consonant_result = max(consonant_map.values(), default=0)
        return vovel_result + consonant_result

s = "successes"

test = Solution()
print(test.maxFreqSum(s))