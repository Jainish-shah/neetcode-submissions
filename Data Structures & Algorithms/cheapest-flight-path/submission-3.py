class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            tempPrices = prices.copy()
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if tempPrices[v] > prices[u] + w:
                    tempPrices[v] = prices[u] + w
            prices = tempPrices
        return -1 if prices[dst] == float('inf') else prices[dst]