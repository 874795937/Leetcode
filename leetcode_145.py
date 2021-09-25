# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        def dfs(node):
            if not node:
                # self.result.append(pre.val)
                return

            dfs(node.left)
            dfs(node.right)
            self.result.append(node.val)

        dfs(root)
        print(self.result)
        return self.result
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)
node5 = TreeNode(6)
node1.right = node2
node2.right= node3
node3.right = node4
node4.right = node5

s = Solution()
s.postorderTraversal(node1)
