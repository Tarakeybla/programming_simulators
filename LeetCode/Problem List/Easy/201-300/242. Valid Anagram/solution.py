class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S_MAP = {}
        T_MAP = {}
        for char_s, char_t in zip(s, t):
            print(char_s, char_t)
            S_MAP[char_s] = S_MAP.get(char_s, 0) + 1
            T_MAP[char_t] = T_MAP.get(char_t, 0) + 1
        return dict(sorted(S_MAP.items())), dict(sorted(T_MAP.items()))


# s = "anagram"
# t = "nagaram"

s = 'a'
t = 'ab'

test = Solution()
print(test.isAnagram(s, t))