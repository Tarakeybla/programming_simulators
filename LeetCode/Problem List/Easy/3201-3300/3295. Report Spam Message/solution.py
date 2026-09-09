# The main difficulty of this exercise is the time limit for execution
# But the exercise itself is very simple, we just need to count the number of times a banned word appears in the message
# I have doubts that this exercise is of medium difficulty...


class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        count: int = 0
        banned_set: set[str] = set(bannedWords)
        for word in message:
            if word in banned_set:
                count += 1
                if count >= 2:
                    return True
        return False
    
test_solution = Solution()
print(test_solution.reportSpam(message = ["t","j","w","g","x","v","b","j"], bannedWords = ["e","q","s","j","q","w","k","w"])) # True 

# The main idea of this solution is to use a set to store the banned words, so that we can check if a word is banned in O(1) time.
# We also keep a count of how many banned words we have seen, and if we see 2 or more, we return True. 
# If we finish checking all the words and we have seen less than 2 banned words, we return False.