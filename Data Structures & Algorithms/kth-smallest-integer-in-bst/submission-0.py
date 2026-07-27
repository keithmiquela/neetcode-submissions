# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: node, stack
# output: stack

# keep going left
# then go up
# then go right
# in order traversal

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, stack):
            if node.left:
                dfs(node.left, stack)
            if len(stack)==k:
                return stack
            stack.append(node.val)
            if node.right:
                dfs(node.right, stack)
            return stack
        return dfs(root, [])[-1]