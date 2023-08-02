# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left -> Root -> Right
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result

