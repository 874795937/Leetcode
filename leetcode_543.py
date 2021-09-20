# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def depth(node):
            if node is None:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            temp = L+R+1
            self.result = max(self.result, L+R+1)
            return max(L, R)+1
        depth(root)
        return self.result-1


root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# node3 = TreeNode(4)
# node4 = TreeNode(5)
# root.left = node1
# root.right = node2
# node1.left = node3
# node1.right = node4
s = Solution()
print(s.diameterOfBinaryTree(root))
