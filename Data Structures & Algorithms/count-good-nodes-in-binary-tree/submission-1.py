# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input max_val
# output good_count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            curr = 0 if node.val < max_val else 1
            max_val = max(max_val, node.val)
            l_count = dfs(node.left, max_val)
            r_count = dfs(node.right, max_val)

            return curr+l_count+r_count
        
        return dfs(root, root.val)

