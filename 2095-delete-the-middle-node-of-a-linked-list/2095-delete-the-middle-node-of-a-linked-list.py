# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        pointer = head
        fast_pointer = head
        prev_pointer = None
        
        while fast_pointer and fast_pointer.next:
            prev_pointer = pointer
            pointer = pointer.next
            fast_pointer = fast_pointer.next.next
        prev_pointer.next = pointer.next
        return head