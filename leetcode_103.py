# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = []
        result = []
        queue.append(root)
        check = 1
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
            if check%2 == 0:
                result.append(list(reversed(temp)))
            else:
                result.append(temp)
            check += 1
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
a = s.zigzagLevelOrder(node1)
print(a)

print(0%2)
