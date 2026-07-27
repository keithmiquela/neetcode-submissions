# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            isSame = True
            if not compare(p.left, q.left):
                isSame = False
            if not compare(p.right, q.right):
                isSame = False
            return isSame
        
        def dfs(node):
            isMatch = False
            if compare(node, subRoot):
                isMatch = True
            if node.left and dfs(node.left):
                isMatch = True
            if node.right and dfs(node.right):
                isMatch = True
            
            return isMatch
        
        return dfs(root)