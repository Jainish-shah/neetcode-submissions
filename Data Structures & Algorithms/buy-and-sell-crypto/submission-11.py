class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minB = prices[0]
        for i in range(len(prices)):
            maxP = max(maxP, prices[i] - minB)
            minB = min(minB, prices[i])
        return maxP
