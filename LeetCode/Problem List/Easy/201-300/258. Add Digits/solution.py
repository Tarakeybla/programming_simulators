class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str(sum([int(num) for num in str_num]))
        return int(str_num)
