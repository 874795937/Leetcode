# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        queue.append(root)
        result = []
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.pop(0)
                if i == length-1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                    print(node.left.val)
                if node.right:
                    print(node.right.val)
                    queue.append(node.right)
        return result

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

s = Solution()
a = s.rightSideView(node1)
print(a)
