# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], parentVal=None) -> int:
        if not root:
            return 0

        if parentVal is None:
            parentVal = root.val
        else:
            parentVal *= 10
            parentVal += root.val

        if root.left is None and root.right is None:
            return parentVal

        return self.sumNumbers(root.left, parentVal) + self.sumNumbers(root.right, parentVal)
