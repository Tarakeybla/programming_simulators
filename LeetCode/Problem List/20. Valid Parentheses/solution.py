# The main idea of this solution is to store values in a dict 
# and uses a stack to determine the result

CHAR_MAP = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for char in s:
            if char in CHAR_MAP.values():
                result.append(char)
            else:
                if not result:
                    return False
                if result.pop() != CHAR_MAP[char]:
                    return False
        return len(result) == 0

# s = "([)]"
# s = "()"
# s = "([])"
# s = "){"
s = "(])"

test_solution = Solution()
print(test_solution.isValid(s))
