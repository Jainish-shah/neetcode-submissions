class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: # [2,3,6,2,4]
        stones = [-s for s in stones] # [-2,-3,....]
        heapq.heapify(stones) # [-6,-4, -3, -2, -2]

        while len(stones) > 1: 
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            diff = x - y
            if diff != 0:   
                heapq.heappush(stones, diff)
        return -stones[0] if stones else 0