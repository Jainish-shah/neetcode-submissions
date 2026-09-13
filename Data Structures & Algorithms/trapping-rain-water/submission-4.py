class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
    
        n = len(height)
        result = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(0,i):
                leftMax = max(leftMax, height[j])

            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])

            result+= min(rightMax, leftMax) - height[i]
        return result