# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = []
        def dfs(root, num):
            if not root:
                return
            num = 10*num+root.val
            if not root.left and not root.right:
                self.result.append(num)
                return
            a = dfs(root.left, num)
            b = dfs(root.right, num)
        dfs(root, 0)
        final = 0
        for item in self.result:
            final += item
        return final
