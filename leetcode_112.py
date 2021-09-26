# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 涉及到叶节点的题都要判断一下
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, target):
            if not root:
                return False

            if not root.left and not root.right:
                if target == 0:
                    return True
            target -= root.val
            return dfs(root.left, target) or dfs(root.right, target)
        result = dfs(root, targetSum)
        return result

node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node7
node4.right = node8
node3.left = node5
node3.right = node6
node6.right = node9

s = Solution()
a = s.hasPathSum(node1, 22)
print(a)
