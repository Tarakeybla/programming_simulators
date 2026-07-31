from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        sorted_count = (
                dict(
                sorted(
                    (Counter(word)).items(),
                    key=lambda value: value[1],
                    reverse=True
                )
            )
        )
        total = 0
        for num, sumb in enumerate(sorted_count.values()):
            if num + 1 <= 8:
                total += sumb
            elif num + 1 <= 16:
                total += sumb * 2
            elif num + 1 <= 24:
                total += sumb * 3
            else:
                total += sumb * 4
        return total


word = 'abcdefghijklmnoprstudsasdasdasdvwxyzz'

test_solution = Solution()
print(test_solution.minimumPushes(word=word))
