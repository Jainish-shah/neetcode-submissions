class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, maxSum = 0, nums[0]
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            maxSum = max(maxSum, sum)
        return maxSum

sol = Solution()
assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6