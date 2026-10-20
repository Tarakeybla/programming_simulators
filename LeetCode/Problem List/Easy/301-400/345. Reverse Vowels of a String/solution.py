class Solution:
    def reverseVowels(self, s: str) -> str:
        char = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        right = len(s)-1
        for left_index in range(len(s)-1):
            if s[left_index].lower() in char and left_index < right:
                for right_index in range(right, 0, -1):
                    if s[right_index].lower() in char:
                        s[left_index], s[right_index] = s[right_index], s[left_index]
                        right = right_index - 1
                        break           
        return ''.join(s)

s = "IceCreAm"

test = Solution()
print(test.reverseVowels(s))

class Solution:
    def reverseVowels(self, s: str) -> str:
        char = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() not in char:
                left += 1
                continue
            if s[right].lower() not in char:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

s = "IceCreAm"

test = Solution()
print(test.reverseVowels(s))