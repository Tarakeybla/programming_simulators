# First solution
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        for kit in self.primitive_decomposition(s):
            result += kit[1:-1]
        return result

    def primitive_decomposition(self, s:str) -> list:
        count_open = 0
        count_close = 0
        parentheses = ''
        result = []
        for parenthes in s:
            if parenthes == '(':
                count_open += 1
            else:
                count_close += 1
        
            parentheses += parenthes
            if count_open == count_close:
                result.append(parentheses)
                parentheses = ''
                count_open, count_close = 0, 0
            
        return result

    
# Second solution
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ''
        for char in s:
            if char == '(':
                if count > 0:
                    result += char
                count += 1
            else:
                count -= 1
                if count > 0:
                    result += char
        return result
