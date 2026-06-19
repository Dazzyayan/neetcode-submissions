# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        i = 0
        while fast:
            fast = fast.next
            if i > n:
                slow = slow.next

            i += 1

        if slow and slow.next:
            slow.next = slow.next.next
        else:
            return None

        return dummy.next
