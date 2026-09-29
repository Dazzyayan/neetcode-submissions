# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que_p = deque()
        que_p.append(p)
        que_q = deque()
        que_q.append(q)
        while len(que_p) > 0:
            if len(que_p) != len(que_q):
                return False
            for _ in range(len(que_p)):
                node_p = que_p.popleft()
                node_q = que_q.popleft()
                p_val = node_p.val if node_p else None
                q_val = node_q.val if node_q else None
                if p_val != q_val:
                    print("p", p_val, "q", q_val)
                    return False
                if node_p:
                    que_p.append(node_p.left)
                    que_p.append(node_p.right)
                if node_q:
                    que_q.append(node_q.left )
                    que_q.append(node_q.right )
        
        return True