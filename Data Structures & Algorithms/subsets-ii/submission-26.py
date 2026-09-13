class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def dfs(cur, i):
            if i == len(nums):
                res.add(tuple(cur))
                return
            if i+1 > len(nums):
                return
            cur.append(nums[i])
            dfs(cur, i+1)
            cur.pop()
            dfs(cur, i+1)    
        dfs([], 0)
        return [list(s) for s in res]