class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            result = n // 2
            n -= result
            count += result
        return count

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1