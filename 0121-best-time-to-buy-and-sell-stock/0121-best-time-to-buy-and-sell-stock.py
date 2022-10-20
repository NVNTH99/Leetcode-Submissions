class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        result = 0
        l = len(prices)
        for i in range(1,l):
            if min > prices[i]:
                min = prices[i]
            elif prices[i] - min > result:
                result = prices[i] - min
        return result