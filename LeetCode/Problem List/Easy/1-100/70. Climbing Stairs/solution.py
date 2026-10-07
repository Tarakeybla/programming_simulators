class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        current = 1

        for _ in range(n):
            prev, current = current, prev + current

        return current
