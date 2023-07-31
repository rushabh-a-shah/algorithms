# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # # ITERATIVE SOLUTION
        # current = head
        # prev = None
        # while current:
        #     temp = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp
        # return prev

        # RECURSIVE SOLUTION
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
