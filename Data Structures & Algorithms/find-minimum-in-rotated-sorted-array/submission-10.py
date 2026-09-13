class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for i in nums:
            if i < mini:
                mini = i
        return mini
















































        # l, r = 0, len(nums)-1
        
        # while l<r:
        #     m = l + (r-l)//2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        # return nums[l]