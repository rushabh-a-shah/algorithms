# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        def inorder_dfs(root):
            if not root:
                return
            inorder_dfs(root.left)
            order.append(root.val)
            inorder_dfs(root.right)
        
        inorder_dfs(root)
        return order[k-1]

    def kthSmallestIterative(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
