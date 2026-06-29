# This solution uses Python's built-in functions.
# int(binary_string, 2) - convert the binary numbers in decimal system
# bin() - convert integer numbers in binary system
# [2:] - skip the two first carakter in bin()

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
