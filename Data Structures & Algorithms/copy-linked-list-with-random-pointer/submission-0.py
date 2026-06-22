"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origRefs = {}
        newNodes = []
        curr = head
        i = 0
        while curr:
            origRefs[curr] = i
            newNodes.append(Node(x=curr.val))
            curr = curr.next
            i += 1
        
        # compose new list
        curr = head
        dummy = Node(x=0)
        p = dummy
        for j, node in enumerate(newNodes):
            if curr.random:
                node.random = newNodes[origRefs[curr.random]]
            p.next = node
            p = p.next
            curr = curr.next
        
        return dummy.next

        
        

        


