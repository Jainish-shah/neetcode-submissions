class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, sum = nums[0], 0
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            max_sum = max(max_sum, sum)
        return max_sum