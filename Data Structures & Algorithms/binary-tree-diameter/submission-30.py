# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res


    #     if not root:
    #         return 0
        
    #     left = self.height(root.left)
    #     right = self.height(root.right)
    #     diameter = left + right
    #     res = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    #     return max(res, diameter)

    # def height(self, cur: Optional[TreeNode]) -> int:
    #     if not cur:
    #         return 0
    #     return 1 + max(self.height(cur.left), self.height(cur.right))
