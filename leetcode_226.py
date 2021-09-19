# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

class Solution1(object):
    def invertTree(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            temp = queue.pop(0)
            temp.left,temp.right = temp.right, temp.left
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return root
        
root = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(6)
node6 = TreeNode(9)
root.left = node1
root.right = node2
node1.left = node6
node1.right = node5
node2.left = node4
node2.right = node3

s = Solution1()
s.invertTree(root)
