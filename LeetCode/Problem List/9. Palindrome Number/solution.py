# The basic idea of ​​my solution is to convert int to str and
# create a variable with the reverse value, then in a loop check 
# the equality of the characters by index.
class Solution:
    def isPalindrome(self, num: int) -> bool:
        str_num = str(num)
        reversed_str_num = str_num[::-1]
        for i in range(len(str_num)):
            if str_num[i] != reversed_str_num[i]:
                return False
        return True

test_solution = Solution()
print(test_solution.isPalindrome(-121))

# But there was a simpler solution....
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False
