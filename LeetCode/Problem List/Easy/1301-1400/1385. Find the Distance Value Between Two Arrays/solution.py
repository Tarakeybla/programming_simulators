class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = len(arr1)
        for char_i in arr1:
            for char_j in arr2:
                if abs(char_i - char_j) <= d:
                    count -= 1
                    break
        return count