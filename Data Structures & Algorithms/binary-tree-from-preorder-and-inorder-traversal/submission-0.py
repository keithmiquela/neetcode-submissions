# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# linked list with reversing
# input: preorder, inorder
# output: node (root)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder:
                return None
            split = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            root.left = dfs(preorder[1:split+1],inorder[0:split])
            root.right = dfs(preorder[split+1:], inorder[split+1:])
            return root
        return dfs(preorder, inorder)