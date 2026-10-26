from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = Counter(s)
        for char in t:
            if char not in s_map or s_map[char] != t.count(char):
                return char
        return ''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:
            if t.count(ch) > s.count(ch):
                return ch
