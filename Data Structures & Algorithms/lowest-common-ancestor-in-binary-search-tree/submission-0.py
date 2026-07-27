# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findMatch(node, find):
            if not node:
                return False
            if findMatch(node.left, find):
                return True
            if findMatch(node.right, find):
                return True
            if node.val == find.val:
                return True
            return False

        def dfs(node):
            if not node:
                return False
            if node.left:
                left = dfs(node.left)
                if left:
                    return left
            if node.right:
                right = dfs(node.right)
                if right:
                    return right
            
            if findMatch(node, p) and findMatch(node, q):
                return node
            
            return None
            
        return dfs(root)
