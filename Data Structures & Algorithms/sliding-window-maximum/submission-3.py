class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r= 0
        q = collections.deque()
        while r < len(nums): # remove useless smaller elements from BACK
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r) # every index is a candidate
            
            if l > q[0]: # evict stale front (slid out of window)
                q.popleft()
            
            if (r+1) >= k: # Front = window max so record it
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        return output
