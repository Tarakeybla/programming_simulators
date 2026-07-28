class Solution:
    def smallestPalindrome(self, s: str) -> str:
        result: list[str | None] = []
        list_s: list[str] = list(s)
        if len(s) <= 1:
            return s
        if len(s) % 2 == 0:
            result.extend(list_s[:int((len(s) / 2))])
            result.sort()
            result.extend(result[::-1])
        else:
            result.extend(list_s[:int((len(s) / 2))])
            result.sort()
            mid_result: list[str] = result[::-1]
            result.append(list_s[int((len(s) // 2))])
            result.extend(mid_result)
        return ''.join(result)


s = 'acbabca'
        
test_solution = Solution()
print(test_solution.smallestPalindrome(s))