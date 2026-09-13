class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            cur = heapq.heappop(stones) - heapq.heappop(stones)
            if cur: 
                heapq.heappush(stones, cur)
        return -stones[0] if stones else 0           