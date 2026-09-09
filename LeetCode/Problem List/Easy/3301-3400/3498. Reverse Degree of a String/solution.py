class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        constant = ord('z')
        for i in range(len(s)):
            total += (abs(ord(s[i]) - constant) + 1) * (i + 1)
        return total
