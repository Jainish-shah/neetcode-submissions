class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we have to maintain both the idle time and characters from the task
        # so we first go with the most frequent task as starting
        # for that we create a hashmap or counter

        count = {}
        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        # taking one element from the maxheap and then putting it in queue for observation
        q = deque() # for storing [-cnt, time + n]
        time = 0
        while maxheap or q:
            time += 1
            if not maxheap:
                time = q[0][1]
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time