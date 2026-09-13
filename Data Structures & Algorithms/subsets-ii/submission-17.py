class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # nums.sort()
        # def dfs(i, subset):
        #     if i == len(nums):
        #         res.append(subset[:])
        #         return
        #     subset.append(nums[i])
        #     dfs(i+1, subset)
        #     subset.pop()
        #     while i+1 < len(nums) and nums[i] == nums[i+1]:
        #         i+=1
        #     dfs(i+1, subset)
        # dfs(0, [])
        # return res


        res = []
        nums.sort()
        def dfs(path, i):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(path, i+1)
            path.pop()            
            while (i+1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            dfs(path, i+1)

        dfs([], 0)
        return res