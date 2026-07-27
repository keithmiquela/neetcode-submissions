# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, length):
            length += 1
            max_length = length
            if node.left:
                max_length=max(max_length,dfs(node.left, length))
            if node.right:
                max_length = max(max_length,dfs(node.right,length))
            return max_length
        
        if not root:
            return 0 
            
        return dfs(root,0)
            
            
