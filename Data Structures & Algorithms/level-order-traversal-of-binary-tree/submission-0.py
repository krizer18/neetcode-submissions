# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        q = collections.deque()
        q.append(root)

        while q:
            curlen = len(q)
            sublist = []
            for i in range(curlen):
                popped = q.popleft()
                if popped:
                    sublist.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if sublist:
                result.append(sublist)

        return result





