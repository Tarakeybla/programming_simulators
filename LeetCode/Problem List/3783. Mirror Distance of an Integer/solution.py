class Solution:
    def mirrorDistance(self, n: int) -> int:
        return n - int(str(n)[::-1])
