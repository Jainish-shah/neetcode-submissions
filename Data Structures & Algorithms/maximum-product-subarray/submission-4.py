class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for i in nums:
            tmp = curMax * i
            curMax = max(curMax * i, i * curMin, i)
            curMin = min(tmp, curMin * i, i)
            res = max(res, curMax)
        return res