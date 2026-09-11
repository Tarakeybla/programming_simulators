from collections import Counter
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        for i in range(100, 1000, 2):
            i_list = [int(x) for x in str(i)]
            if not (Counter(i_list) - Counter(digits)):
                count += 1
        return count
