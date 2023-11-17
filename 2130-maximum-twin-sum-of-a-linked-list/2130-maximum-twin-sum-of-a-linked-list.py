# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0
        values = []
        current = head
        index = 0
        while current:
            values.append(current.val)
            current = current.next
            index += 1
        twin_sums = set()
        current = head
        index = 0
        while current:
            twin_index = len(values) - 1 - index
            twin_sums.add(current.val + values[twin_index])
            current = current.next
            index += 1
        return max(twin_sums)
        
