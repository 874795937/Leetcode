# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        if head is None:
            return None

        while 1:
            stack.append(head)
            head = head.next
            if head is None:
                break

        head = stack.pop()
        result = head
        while 1:
            if not stack:
                break
            head.next = stack.pop()
            head = head.next
        head.next = None
        return result

class Solution1(object):
    def reverseList(self, head):
        if head is None:
            return None
        pre = None
        self.result = None
        def reverse(node, pre):
            if node.next is None:
                node.next = pre
                self.result = node
            else:
                nextNode = node.next
                node.next = pre
                pre = node
                reverse(nextNode, pre)
        reverse(head, pre)
        return self.result

class Solution2(object):
    def reverseList(self, head):
        preNode = None
        result = None
        if head is None:
            return None
        while 1:
            nextNode = head.next
            head.next = preNode
            preNode = head
            if nextNode is None:
                result = head
                break
            head = nextNode
        return result

class Solution3(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution3()
head = s.reverseList(node1)
# print(node1.next.val)
while head:
    print(head.val)
    head = head.next
