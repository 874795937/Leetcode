# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            result.append(stack.pop())
        # print(result)
        return result

class Solution(object):
    def reversePrint(self, head):
        self.result = None
        list = []
        def reverse(head, pre):
            if head is None:
                self.result = pre
                return
            nextNode = head.next
            head.next = pre
            pre = head
            reverse(nextNode, pre)
        reverse(head, None)
        while self.result:
            list.append(self.result.val)
            self.result = self.result.next
        return list

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.reversePrint(node1))
