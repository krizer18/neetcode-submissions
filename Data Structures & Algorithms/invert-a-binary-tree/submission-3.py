# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        if root.right == None and root.left == None:
            return root

        elif root.right == None:
            self.invertTree(root.left)
            root.right = root.left
            root.left = None

        elif root.left == None:
            self.invertTree(root.right)
            root.left = root.right
            root.right = None
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp

        return root
