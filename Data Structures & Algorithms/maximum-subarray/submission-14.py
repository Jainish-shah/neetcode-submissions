class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        for i in range(0, n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                maxSum = max(maxSum, cur)
        return maxSum