# Functional solution
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         prew = []
#         while n != 1 and n not in prew:
#             n
#             current = 0
#             prew.append(n)
#             for num in [int(num) for num in str(n)]:
#                 current += num ** 2
#             n = current
#         if n == 1:
#             return True 
#         else:
#             return False


# Class solution
class Solution:
    def __init__(self):
        self.prev = []

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n in self.get_prev():
            return False
        self.save_prev(n)
        current = 0
        for num in [int(num) for num in str(n)]:
            current += num ** 2
        return self.isHappy(current)

    def save_prev(self, current: int) -> list:
        self.prev.append(current)

    def get_prev(self) -> list:
        return self.prev


n = 10

test = Solution()
print(test.isHappy(n))