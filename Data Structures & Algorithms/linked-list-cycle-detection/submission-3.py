# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        if not fast:
                return False
        fast = fast.next
        slow = head.next

        while fast != slow:
            if not fast:
                return False
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next
            
        
        return True

        
