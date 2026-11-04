class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # moving from the back of the List
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)