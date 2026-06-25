# This solution uses the split() method, which splits a string
# into words using whitespace characters by default.
# We then return the length of the last element in the resulting list.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len((s.split())[-1])
    
test_solution = Solution()

# s = "Hello World"
s = "   fly me   to   the moon  "

print(test_solution.lengthOfLastWord(s))