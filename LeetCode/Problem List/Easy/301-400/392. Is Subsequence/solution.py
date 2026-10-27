class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        positions = 0
        result = []
        for char in s:
            for index in range(positions, len(t)):
                if char == t[index]:
                    positions = index + 1
                    result.append(index)
                    break
        if len(result) == len(s) and result == sorted(result):
            return True
        return False   


# s = "axc"
# t = "aahcxbgdcx"

s = "aaaaaa"
t = "bbaaaa"

test = Solution()
print(test.isSubsequence(s, t))


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for ch in t:
            if left < len(s) and s[left] == ch:
                left += 1
        return left == len(s)