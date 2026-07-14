class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total_count: int = 0
        count_r: int = 0
        count_l: int = 0
        for character in s:
            if character == 'R':
                count_r += 1
            else:
                count_l += 1

            if count_r == count_l:
                total_count += 1
                count_r, count_r = 0, 0
        return total_count


s = "RLRRLLRLRL"

test_solution = Solution()
print(test_solution.balancedStringSplit(s))
