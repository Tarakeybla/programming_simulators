MORSE_MAP = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.', 
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        result = set()
        for word in words:
            morse_word = ''
            for char in word:
                morse_word += MORSE_MAP[char]
            result.update(morse_word)
        return len(result)
    

words = ["gin","zen","gig","msg"]

test = Solution()
print(test.uniqueMorseRepresentations(words))



class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            morse_word = ""
            for char in word:
                morse_word += morse[ord(char) - ord('a')]
            
            result.update(morse_word)
                
        return len(result)

words = ["gin","zen","gig","msg"]

test = Solution()
print(test.uniqueMorseRepresentations(words))