# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 and list2):
            return list1 if list1 else list2

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        curr = head
        cl1 = list1
        cl2 = list2
        while cl1 and cl2:
            if cl1.val <= cl2.val:
                next = cl1
                cl1 = cl1.next
            else:
                next = cl2
                cl2 = cl2.next
            
            curr.next = next
            curr = curr.next
        if cl1:
            curr.next = cl1
        else:
            curr.next = cl2
        
        return head
