# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: node, minVal, maxVal
# output: isValid
# edge cases: traversing left, right, and in the middle
# node is None
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            if not node:
                return True
            if not (node.val > minVal and node.val < maxVal):
                return False
            isLeftValid = dfs(node.left, minVal, node.val)
            isRightValid = dfs(node.right, node.val, maxVal)
            return isLeftValid and isRightValid

        return dfs(root, -1001, 1001)