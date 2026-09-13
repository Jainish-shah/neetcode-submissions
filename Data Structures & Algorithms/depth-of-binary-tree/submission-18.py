# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, 1]]
        while stack:
            node, val = stack.pop()
            if node:
                res = max(res, val)
                stack.append([node.left, 1+val])
                stack.append([node.right,1+val])
        return res