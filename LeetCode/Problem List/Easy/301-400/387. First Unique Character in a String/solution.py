class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index in range(len(s)):
            if s.count(s[index]) == 1:
                return index
        return -1


import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1