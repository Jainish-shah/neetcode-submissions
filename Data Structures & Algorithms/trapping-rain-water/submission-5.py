class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        n = len(height)
        for i in range(n):
            leftmax = rightmax = height[i]
            for j in range(i):
                leftmax = max(leftmax, height[j])
            for k in range(i+1, n):
                rightmax = max(rightmax, height[k])
            res += min(rightmax, leftmax) - height[i]
        return res