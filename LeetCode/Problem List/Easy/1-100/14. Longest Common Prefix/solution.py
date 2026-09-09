# The main idea of this solution is to sort the input list
# and compare the first and last strings character by character.
# Since these strings differ the most after sorting, their common prefix
# is also the common prefix of all strings in the list.

# Edge cases are handled before entering the loop.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        strs.sort()
        output = ''
        if len(strs) <= 1 and len(strs[0]) <= 1:
            return strs[0]
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                output += strs[0][i]
            else:
                break
        return output

# strs = ["flower","flow","flight", "flo"]
# strs = [""]
# strs = ["",""]
strs = ["b", "a"]

test_solution = Solution()
print(test_solution.longestCommonPrefix(strs=strs))
