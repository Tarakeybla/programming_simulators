class Solution:
    def smallestPalindrome(self, s: str) -> str:
        result: list[str | None] = []
        list_s: list[str] = list(s)
        if len(s) <= 1:
            return s
        
        result.extend(list_s[:int((len(s) / 2))])
        result.sort()

        if len(s) % 2 == 0:
            result.extend(result[::-1])
        else:
            second_half: list[str] = result[::-1]
            result.append(list_s[int((len(s) / 2))])
            result.extend(second_half)
        return ''.join(result)


s = 'acbabca'
        
test_solution = Solution()
print(test_solution.smallestPalindrome(s))