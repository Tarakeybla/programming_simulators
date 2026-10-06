class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        if '(' not in s or ')' not in s:
            return len(s)

        s = list(s)
        count = 0
        while len(s) != 0:
            current = s[0]
            if current == ')':
                count += 1
                del s[0]
            else:
                for index in range(1, len(s)):
                    if s[index] == ')':
                        del s[index]
                        del s[0]
                        break
                if '(' not in s or ')' not in s:
                    count += len(s)
                    break
        return count
