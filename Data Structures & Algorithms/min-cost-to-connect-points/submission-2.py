class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)} # to store the [cost, point]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0 # total cost
        minHeap = [[0, 0]] # cost, point
        visit = set()
        while len(visit) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            res += cost
            visit.add(point)
            for neiCost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res