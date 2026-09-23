class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 1:
            for i in range(1, 31):
                if n / 2**i == 1.0:
                    return True
            return False
        elif n == 1 :
            return True
        elif n < 1:
            return False


        return n > 0 and (n & (n - 1)) == 0