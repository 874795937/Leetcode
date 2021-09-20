# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                pre = pre.next
                head = head.next
        return dummy.next

class Solution1(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        def remove(node, val, pre):
            if node is None:
                return 0
            if node.val == val:
                pre.next = node.next
                node = node.next
            else:
                pre = pre.next
                node = node.next
            remove(node, val, pre)
        remove(head, val, dummy)
        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(4)
node6 = ListNode(6)
node7 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution1()
head = s.removeElements(node1, 4)
while head:
    print(head.val)
    head = head.next
