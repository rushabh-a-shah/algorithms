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
        node_map = { None : None}
        current = head
        while current:
            new = Node(current.val)
            node_map[current] = new
            current = current.next
        
        current = head
        while current:
            copy = node_map[current]
            copy.next = node_map[current.next]
            copy.random = node_map[current.random]
            current = current.next
        
        return node_map[head]

