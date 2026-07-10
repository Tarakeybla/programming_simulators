matrix = [[0,1,1],[1,0,1],[1,1,0]]

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans: list = [0 for num in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0:
                    ans[i] += matrix[i][j]
        return ans

test_solution = Solution()
print(test_solution.findDegrees(matrix))

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(nums) for nums in matrix]

test_solution = Solution()
print(test_solution.findDegrees(matrix))
