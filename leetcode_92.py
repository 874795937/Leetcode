# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pre = None
        cur = head
        num = 1
        leftNode = None
        left1Node = None
        rightNode = None
        right1Node = None
        dummy = ListNode(0)
        dummy.next = head
        while cur:
            curNext = cur.next
            if num >= left and num <= right:
                cur.next = pre
            if num == left-1:
                leftNode = cur
            if num == left:
                left1Node = cur
            if num == right:
                right1Node = cur
            if num == right+1:
                rightNode = cur

            pre = cur
            cur = curNext
            num += 1
        if leftNode and right1Node:
            leftNode.next = right1Node
        if left1Node and right1Node:
            left1Node.next = rightNode
        if leftNode:
            return dummy.next
        else:
            return right1Node
        # while leftNode:
        #     print(leftNode.val)
        #     leftNode = leftNode.next

        # while pre:
        #     print(pre.val)
        #     pre = pre.next
node0 = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node6 = ListNode(6)

node0.next = node1
node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6

# while node1:
#     print(node1.val)
#     node1 = node1.next
s = Solution()
a = s.reverseBetween(node0, 3, 3)
while a:
    print(a.val)
    a = a.next
