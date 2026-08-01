# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            
            height_l = dfs(node.left) 
            height_r = dfs(node.right)

            self.res = max(self.res, height_l + height_r)
            return 1 + max(height_l, height_r)
        dfs(root)
        return self.res






