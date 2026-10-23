class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_map = {}
        for char in ransomNote:
            ransomNote_map[char] = ransomNote_map.get(char, 0) + 1

        print(ransomNote_map)

        for char in magazine:
            if char in ransomNote_map:
                if ransomNote_map[char] != 0:
                    ransomNote_map[char] -= 1

        print(ransomNote_map)

        for value in ransomNote_map.values():
            if value != 0:
                return False

        return True

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

test = Solution()
print(test.canConstruct(ransomNote, magazine))

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for chr in set(ransomNote):
            if ransomNote.count(chr) > magazine.count(chr):
                return False
        return True