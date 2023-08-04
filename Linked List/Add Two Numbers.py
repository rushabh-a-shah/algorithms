# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current_new = dummy

        while l1 or l2 or carry:
            current_new.next = ListNode()
            current_new = current_new.next

            current = carry

            if not l1 and not l2:
                current = carry
            elif not l1:
                current = l2.val + carry
            elif not l2:
                current = l1.val + carry
            else:
                current = l1.val + l2.val + carry
            carry = current // 10
            current = current % 10

            current_new.val = current

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
