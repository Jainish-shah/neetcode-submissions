# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        # return the max path value w/o split
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(rightMax, leftMax)

        dfs(root)
        return res