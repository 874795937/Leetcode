# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(4)

node4 = TreeNode(1)
node5 = TreeNode(2)
node6 = TreeNode(3)

node1.left = node2
node1.right = node3

node4.left = node5
node4.right = node6
s = Solution()
result = s.isSameTree(node1, node4)
print(result)
