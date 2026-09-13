class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        n = len(heights)
        for i in range(n):
            h = heights[i]

            r = i + 1
            while r < n and h <= heights[r]:
                r += 1
            
            l = i
            while l >= 0 and h <= heights[l]:
                l -= 1    
            r -= 1
            l += 1
            maxarea = max(maxarea, h * (r - l + 1))
        return maxarea