class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for char in s.lower():
            if char.isalpha() or char.isdigit():
                result += char
        return True if result == result[::-1] else False


# s = "race a car"
s = "A man, a plan, a canal: Panama"

test = Solution()
print(test.isPalindrome(s))