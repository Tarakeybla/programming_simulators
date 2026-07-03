# The core idea of this solution is to determine whether the current number
# is greater than the previous one.

# If it is, we subtract twice the previous number from the current number
# to offset the value that has already been added to the accumulated result.

ROMAN_NUMERAL_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            if i > 0 and ROMAN_NUMERAL_MAP[s[i]] > ROMAN_NUMERAL_MAP[s[i - 1]]:
                total += ROMAN_NUMERAL_MAP[s[i]] - (ROMAN_NUMERAL_MAP[s[i - 1]] * 2)
            else:
                total += ROMAN_NUMERAL_MAP[s[i]]
        return total

test_solution = Solution()
print(test_solution.romanToInt("MCMXCIV"))
