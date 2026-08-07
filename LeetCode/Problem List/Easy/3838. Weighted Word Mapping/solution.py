from typing import List


REVERS_LETTERS_MAP = {
    25: 'a',
    24: 'b',
    23: 'c',
    22: 'd',
    21: 'e',
    20: 'f',
    19: 'g',
    18: 'h',
    17: 'i',
    16: 'j',
    15: 'k',
    14: 'l',
    13: 'm',
    12: 'n',
    11: 'o',
    10: 'p',
    9: 'q',
    8: 'r',
    7: 's',
    6: 't',
    5: 'u',
    4: 'v',
    3: 'w',
    2: 'x',
    1: 'y',
    0: 'z'
}

LETTERS_MAP = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result: list = []
        for i in range(len(words)):
            total_for_letter = 0
            for letter in words[i]:
                total_for_letter += weights[LETTERS_MAP[letter]]
            result.append(REVERS_LETTERS_MAP[total_for_letter % 26])
        return ''.join(result)


words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

test_solution = Solution()
print(test_solution.mapWordWeights(words=words, weights=weights))
