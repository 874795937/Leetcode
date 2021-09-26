# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def dfs(left, right):
            if left is None and right is None:
                return True
            if (left is None and right is not None) or (left is not None and right is None):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(right.left, left.right)
        return dfs(root.left, root.right)


class Solution1(object):
    def isSymmetric(self, root):
        if not root:
            return True
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if left is None and right is None:
                continue
            if (left is None and right is not None) or (left is not None and right is None):
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

class Solution2(object):
    def isSymmetric(self, root):
        if not root.left and not root.right:
            return True
        if (not root.left and root.right) or (root.left and not root.right):
            return False

        def dfs(left, right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.right, right.left) and dfs(left.left, right.right)
        return dfs(root.left, root.right)
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(1)
node5 = TreeNode(1)
node6 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node6
node1.right = node5
node2.left = node4
node2.right = node3
s = Solution1()
print(s.isSymmetric(root))
