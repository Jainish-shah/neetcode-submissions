class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            height = heights[i]
            r = i + 1
            while r < n and height <= heights[r]:
                r += 1
            l= i
            while l >= 0 and height <= heights[l]:
                l -= 1
            
            r -= 1
            l += 1
            maxArea = max(maxArea, height*(r - l + 1))
        return maxArea