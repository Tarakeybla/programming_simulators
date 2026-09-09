# This solution uses a simple approach to convert the list of digits into an integer, 
# add one to it, and then convert it back into a list of digits.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        solid_digits = ''.join(map(str, digits))
        return list(map(int, str(int(solid_digits) + 1)))

digits = [1,2,3]

test_solution = Solution()
print(test_solution.plusOne(digits))

# In the future, it is necessary to rewrite this problem into an algorithmic solution.
