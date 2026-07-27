# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0,0]
            r_len, r_d = dfs(node.right)
            l_len, l_d = dfs(node.left)
            max_len = max(r_len + 1, l_len +1)
            max_d = max(r_len + l_len + 1, r_d, l_d)
            return [max_len, max_d]

        return dfs(root)[1] - 1

