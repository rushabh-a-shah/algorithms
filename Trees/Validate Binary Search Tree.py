# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validDFS(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if not (leftBoundary < node.val < rightBoundary):
                return False
            
            return validDFS(node.left, leftBoundary, node.val) and validDFS(node.right, node.val, rightBoundary)
        
        return validDFS(root, -math.inf, math.inf)
