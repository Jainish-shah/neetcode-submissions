class Solution:
    # Input: candidates = [9,2,2,4,6,1,5], target = 8

    # Output: [
    # [1,2,5],
    # [2,2,4],
    # [2,6]
    # ]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if len(candidates) == i or target < total:
                return
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res