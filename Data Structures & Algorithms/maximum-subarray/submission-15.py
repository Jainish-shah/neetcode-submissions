class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxV = nums[0]
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                maxV = max(maxV, cur)
        return maxV