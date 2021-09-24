# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        Root = TreeNode(0)
        dummy.left = Root
        def merge(node1, node2, node):
            node4 = TreeNode(0)
            node3 = TreeNode(0)
            if node1 and node2:
                node.val = node1.val+node2.val
                if node1.left or node2.left:
                    node.left = node3
                if node1.right or node2.right:
                    node.right = node4
                merge(node1.right, node2.right, node4)
                merge(node1.left, node2.left, node3)
            elif not node1 and node2:
                print("2444444444444444")
                node.val = node2.val
                if node2.left:
                    node.left = node3
                if node2.right:
                    node.right = node4
                merge(None, node2.right, node4)
                merge(None, node2.left, node3)
            elif node1 and not node2:
                print("23333333333333")
                node.val = node1.val
                if node1.left:
                    node.left = node3
                if node1.right:
                    node.right = node4
                merge(node1.right, None, node4)
                merge(node1.left, None, node3)
            else:
                return 0

        merge(root1, root2, Root)
        return Root

class Solution1(object):
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        merged = TreeNode(root1.val+root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(5)

node5 = TreeNode(2)
node6 = TreeNode(1)
node7 = TreeNode(3)
node8 = TreeNode(4)
node9 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4

node5.left = node6
node5.right = node7
node6.right = node8
node7.right = node9

s = Solution1()
root = s.mergeTrees(node1, node5)
# print(root.val)
def printNode(root):
    if not root:
        return 0
    print(root.val)
    printNode(root.left)
    printNode(root.right)
printNode(root)
# print(root.left.right.val)
