# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Bredth First Search 
        res = 0
        q = collections.deque()
        q.append([root, float('-inf')])
        while q:
            root, maxV = q.popleft()
            if root:
                res += 1 if root.val >= maxV else 0
                maxV = max(maxV, root.val)
                q.append([root.left, maxV])
                q.append([root.right, maxV])
        return res
        # Depth First Search
        # def dfs(root, maxV):
        #     if not root:
        #         return 0
        #     count = 1 if maxV <= root.val else 0
        #     maxV = max(maxV, root.val)
        #     count += dfs(root.left, maxV)
        #     count += dfs(root.right, maxV)
        #     return count
        # return dfs(root, root.val)

        