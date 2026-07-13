class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        result_list: list[int] = []
        for person in order:
            if person in friends:
                result_list.append(person)
        return result_list


order = [3,1,2,5,4]
friends = [1,3,4]

test_solution = Solution()
print(test_solution.recoverOrder(order=order, friends=friends))
