class Solution:
    def interpret(self, command: str) -> str:
        prev = ''
        result = ''
        for char in command:
            if prev == '(' and char == ')':
                result += 'o'
            elif char != '(' and char != ')':
                result += char
            prev = char
        return result


command = "G()(al)"


test = Solution()
print(test.interpret(command))


class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command