class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        for char in bin(x^y)[2:]:
            if char == '1':
                counter += 1
        return counter


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
