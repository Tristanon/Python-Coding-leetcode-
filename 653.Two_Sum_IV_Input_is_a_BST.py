# 653.Two_Sum_IV_Input_is_a_BST.py
# Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        s = set()
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val in s:
                return True
            s.add(k - node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

         