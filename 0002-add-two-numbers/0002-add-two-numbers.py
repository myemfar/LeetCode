# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        cur_node = l1
        while cur_node.next:
            num1.append(cur_node.val)
            cur_node = cur_node.next
        num1.append(cur_node.val)
        cur_node = l2
        while cur_node.next:
            num2.append(cur_node.val)
            cur_node = cur_node.next
        num2.append(cur_node.val)
        num1.reverse()
        num2.reverse()
        def convert(nums):
            string_list = [str(num) for num in nums]
            result = ''.join(string_list)
            return int(result)
        numsum = convert(num1) + convert(num2)
        sumdigits = [int(digit) for digit in str(numsum)]
        sumdigits.reverse()
        def create_ll(digits):
            if not digits:
                return None
            head = ListNode(digits[0])
            current = head
            for digit in digits[1:]:
                current.next = ListNode(digit)
                current = current.next
            return head
        result = create_ll(sumdigits)
        return result
        
                
