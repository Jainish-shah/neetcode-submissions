# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        tokens = []

        # Record each node before its children and mark missing children.
        def preorder(node):
            if node is None:
                tokens.append("N")
                return

            tokens.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(tokens)

    def deserialize(self, data):
        tokens = iter(data.split(","))

        # Read tokens in preorder and rebuild the matching subtree.
        def build_tree():
            token = next(tokens)

            # A null marker represents an absent child.
            if token == "N":
                return None

            # Create the node and recursively build both children.
            node = TreeNode(int(token))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()