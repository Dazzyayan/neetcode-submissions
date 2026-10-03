# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pv = p.val
        qv = q.val

        curr = root
        both_left = pv < curr.val and qv < curr.val
        both_right = pv > curr.val and qv > curr.val
        while both_left or both_right:
            if both_left:
                curr = curr.left
            if both_right:
                curr = curr.right
            
            both_left = pv < curr.val and qv < curr.val
            both_right = pv > curr.val and qv > curr.val
        
        return curr


