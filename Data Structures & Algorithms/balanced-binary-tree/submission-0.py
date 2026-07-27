# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, length):
            if not node:
                return [True, 0]

            l_isBal, l_len = dfs(node.left, length)
            r_isBal, r_len = dfs(node.right, length)

            if not l_isBal or not r_isBal:
                return [False, 0]

            isBal = abs(l_len - r_len) <= 1

            length = max(l_len, r_len)
            
            return [isBal, length+1]
        
        return dfs(root, 0)[0]
            