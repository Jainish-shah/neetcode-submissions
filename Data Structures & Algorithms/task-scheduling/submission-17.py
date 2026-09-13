class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for c in tasks:
            count[c] = 1 + count.get(c, 0)
        
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while q or maxheap:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxheap) + 1
                if cnt:
                    q.append([cnt, time+n])
            if q and time == q[0][1]:
                cnt, time = q.popleft()
                heapq.heappush(maxheap, cnt)
        return time