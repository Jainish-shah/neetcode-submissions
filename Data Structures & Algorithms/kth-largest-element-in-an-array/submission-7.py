class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # arr = [-s for s in nums]
        # heapq.heapify(arr)
        # while k > 1:
        #     heapq.heappop(arr)
        #     k -=1
        # return -arr[0]

        nums.sort()
        return nums[len(nums) - k]