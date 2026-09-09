# This is solution used a native python function to the find the index.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

haystack = "sadbutsad"
needle = "sad"

test_solution = Solution()
print(test_solution.strStr(haystack, needle))
