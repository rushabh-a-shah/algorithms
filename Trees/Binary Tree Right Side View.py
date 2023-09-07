# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        if root:
            q.append(root)

        while q:
            lenQ = len(q)
            visible = None
            for _ in range(lenQ):
                visible = q.popleft()
                if visible.left:
                    q.append(visible.left)
                if visible.right:
                    q.append(visible.right)
            res.append(visible.val)
        
        return res
