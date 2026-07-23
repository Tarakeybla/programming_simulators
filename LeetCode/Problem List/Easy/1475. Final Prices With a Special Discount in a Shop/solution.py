class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = []
        while len(prices) > 0:
            start_price = prices.pop(0)
            flag = False
            for discount in prices:
                if start_price >= discount:
                    flag = True
                    result.append(start_price - discount)
                    break
            if not flag:
                result.append(start_price)
        return result


prices = [8,4,6,2,3]

test_solution = Solution()
print(test_solution.finalPrices(prices))
