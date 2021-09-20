# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#stack
# 要考虑翻转之后的最后一个Node,可能依然指向的是之前的Node,导致cycle
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        stack = []
        stack.append(head)
        while head.next:
            stack.append(head.next)
            head = head.next
        head = stack.pop()
        result = head
        while stack:
            head.next = stack.pop()
            head = head.next
        head.next = None
        return result

# 迭代（双指针）
class Solution1(object):
    def reverseList(self, head):
        preNode = None
        while head:
            temp = head.next
            head.next = preNode
            # if head.next is not None:
            #     print(head.next.val)
            preNode = head
            head = temp
            if head is None:
                return preNode

# 递归
class Solution2(object):
    def reverseList(self, head):
        self.result = None
        def reverse(node, pre):
            if node.next:
                temp = node.next
                node.next = pre
                pre = node
                reverse(temp, pre)
            else:
                node.next = pre
                self.result = node
        if head is None:
            return head
        reverse(head, None)
        return self.result

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution2()
head = s.reverseList(node1)
# print(node1.next.val)
while head:
    print(head.val)
    head = head.next
