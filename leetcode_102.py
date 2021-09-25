# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# queue可以储存None值
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        result = []
        queue.append(root)
        while queue:
            node = []
            temp = []
            for i in range(len(queue)):
                node.append(queue.pop(0))
                temp.append(node[i].val)
            result.append(temp)
            for i in range(len(node)):
                if node[i].left:
                    queue.append(node[i].left)
                if node[i].right:
                    queue.append(node[i].right)
        return result

class Solution1(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)
        print(result)

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

s = Solution1()
s.levelOrder(node1)
