class Solution:
    def maxDistinct(self, s: str) -> int:
        uniq_character = []
        for charact in s:
            if charact in uniq_character:
                continue
            else:
                uniq_character.append(charact)
        return len(uniq_character)
