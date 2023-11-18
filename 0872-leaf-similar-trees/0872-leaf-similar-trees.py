# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_values(root, values):
            if not root:
                return
            if not root.left and not root.right:
                values.append(root.val)
            get_leaf_values(root.left, values)
            get_leaf_values(root.right, values)
        leaf_values1 = []
        leaf_values2 = []
        get_leaf_values(root1, leaf_values1)
        get_leaf_values(root2, leaf_values2)
        return leaf_values1 == leaf_values2