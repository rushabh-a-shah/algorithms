# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        maxNode = -math.inf

        def dfs(node, maxNode):
            if not node:
                return
            if node.val >= maxNode:
                self.res += 1
                maxNode = node.val
            
            dfs(node.left, maxNode)
            dfs(node.right, maxNode)
        
        dfs(root, maxNode)
        return self.res

