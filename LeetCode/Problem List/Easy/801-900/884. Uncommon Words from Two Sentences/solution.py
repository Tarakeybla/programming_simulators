class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]: 
        char_count = {}
        for char in s1.split():
            char_count[char] = char_count.get(char, 0) + 1
        for char in s2.split():
            char_count[char] = char_count.get(char, 0) + 1
        return [char[0] for char in char_count.items() if char[1] == 1]


from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        return [char for char, value in (Counter(s1.split() + s2.split())).items() if value == 1]
