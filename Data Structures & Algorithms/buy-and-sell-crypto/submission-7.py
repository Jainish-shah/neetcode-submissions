class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxP = 0
        # minBuy = prices[0]

        # for sell in prices:
        #     maxP = max(maxP, sell - minBuy)
        #     minBuy = min(minBuy, sell)
        # return maxP


        maxP = 0
        minBuy = prices[0]
        for i in prices:
            maxP = max(maxP, i - minBuy)
            minBuy = min(minBuy, i)
        return maxP