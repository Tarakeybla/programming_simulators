# My solution
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        total = 0
        for key, value in (self.count_characters(n)).items():
            total += key * value
        return total
    
    def count_characters(self, num: int) -> dict:
        character_maps: dict = {}
        for num in str(n):
            num = int(num)
            if num not in character_maps.keys():
                character_maps[num] = 0
            character_maps[num] += 1 
        return character_maps

n = 122

test_solution = Solution()
print(test_solution.digitFrequencyScore(n))

# The perfect solution
from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum({key: value * int(key) for key, value in Counter(str(n)).items()}.values())

n = 122

test_solution = Solution()
print(test_solution.digitFrequencyScore(n))