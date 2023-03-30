# 94.Binary_Tree_Inorder_Traversal.py
# Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            array.append(root.val)
            dfs(root.right)
        dfs(root)
        return array