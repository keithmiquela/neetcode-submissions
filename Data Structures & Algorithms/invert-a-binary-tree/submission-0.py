# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def switch(node):
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                switch(node.left)
            
            if node.right:
                switch(node.right)
        if not root:
            return None
            
        switch(root)

        return root