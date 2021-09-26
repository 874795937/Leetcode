# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                return 1
            val1 = dfs(node.left)
            val2 = dfs(node.right)
            if val1 and val2:
                return min(val1+1, val2+1)
            elif val1 and not val2:
                return val1+1
            elif not val1 and val2:
                return val2+1

        depth = dfs(root)
        return depth


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node4.right = node5
s = Solution()
s.minDepth(node1)
