class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
    

haystack = "sadbutsad"
needle = "sad"

test_solution = Solution()
print(test_solution.strStr(haystack, needle))
