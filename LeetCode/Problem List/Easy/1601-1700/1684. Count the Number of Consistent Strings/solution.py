allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for char in word:
                if char not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count

test = Solution()
print(test.countConsistentStrings(allowed=allowed, words=words))