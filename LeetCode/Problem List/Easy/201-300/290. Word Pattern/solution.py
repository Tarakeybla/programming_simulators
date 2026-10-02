class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        WORD_MAP = {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for index, char in enumerate(pattern):
            if char not in WORD_MAP and words[index] not in WORD_MAP.values():
                WORD_MAP[char] = words[index]
            else:
                if WORD_MAP.get(char) != words[index]:
                    return False
        return True