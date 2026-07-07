from math import sqrt

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
    
test_solution = Solution()
print(test_solution.mySqrt(8))


class SolutionTwo:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        r = x // 2
        while r * r > x:
            r = (r + x // r) // 2
        
        return r