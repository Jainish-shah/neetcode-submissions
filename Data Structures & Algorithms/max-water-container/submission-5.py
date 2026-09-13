class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                maxA = max(maxA, min(heights[i], heights[j]) * (j-i))
        return maxA