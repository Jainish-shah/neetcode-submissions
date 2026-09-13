class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        dist[k-1] = 0
        for _ in range(n-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = w + dist[u-1]
        res = max(dist)
        return res if float('inf') > res else -1