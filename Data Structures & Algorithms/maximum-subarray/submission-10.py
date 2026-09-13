class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        res = 0
        for i in nums:
            if res < 0:
                res = 0
            res = i + res
            maxS = max(maxS, res)
        return maxS