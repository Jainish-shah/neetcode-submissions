class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        arr = nums1 + nums2
        total = m + n
        arr.sort()

        if total % 2 == 0:
            return (arr[total//2 - 1] + arr[total//2])/2.0
        else:
            return (arr[total//2])