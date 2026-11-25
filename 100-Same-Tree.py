# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BFS:广度优先搜索
        from collections import deque
        qu=deque()
        if not p and not q:
            return True
        elif not p or not q:
            return False
        qu.append((p,q))
        while qu:
            a,b=qu.popleft()
            if not a and not b:
                continue
            elif not a or not b:
                return False
            elif a.val!=b.val:
                return False
            # 两棵树的左节点和左节点比较 右节点和右节点比较
            qu.append((a.left,b.left))
            qu.append((a.right,b.right))
        return True
