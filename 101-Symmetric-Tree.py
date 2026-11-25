# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        #DFS:深度优先搜索
        if not root:
            return True
        stack=[]
        stack.append((root.left,root.right))
        while stack:
            left,right=stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val!=right.val:
                return False
            # 因为要判断对称:左节点的左节点和右节点的右节点配对 左节点的右节点和右节点的左节点配对
            stack.append((left.left,right.right))
            stack.append((left.right,right.left))
        return True
