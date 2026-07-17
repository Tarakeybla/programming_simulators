class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for base in range(2, n - 1):
            res = ''
            num = n
            while num > 0:
                res += digits[num % base]
                num //= base
            if res != res[::-1]:
                return False
        return True


n = 4

test_solution = Solution()
print(test_solution.isStrictlyPalindromic(n))
