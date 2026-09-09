class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prev = prices[0]
        result = 0
        for index in range(1, len(prices)):
            current = prices[index]
            if current >= prev:
                difference = current - prev
                if difference > result:
                    result = difference
            else:
                prev = prices[index]