class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        result = 0
        for i in prices[1:]:
            if min > i:
                min = i
            elif i - min > result:
                result = i - min
        return result