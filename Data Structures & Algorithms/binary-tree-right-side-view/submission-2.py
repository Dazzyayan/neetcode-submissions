# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        q = deque()
        q.append(root)

        while len(q) > 0:
            row_length = len(q)
            for i in range(row_length):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                    if i == row_length - 1:
                        out.append(node.val)
        
        return out