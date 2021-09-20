# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        point1 = l1
        point2 = l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = None
        while point1 and point2:
            if point1.val <= point2.val:
                if head is None:
                    head = point1
                    # print(head.val,"23333")
                    result = head
                    point1 = point1.next
                else:
                    head.next = point1
                    head = head.next
                    # print(head.val,"24444")
                    point1 = point1.next
            else:
                if head is None:
                    head = point2
                    # print(head.val,"25555")
                    result = head
                    point2 = point2.next
                else:
                    head.next = point2
                    head = head.next
                    # print(head.val,"26666")
                    point2 = point2.next
        # print(point1.val,"point1")
        # print(point2.val,"point2")
        # print(head.val,"head")
        if point1 is None:
            head.next = point2
        if point2 is None:
            head.next = point1
        return result

class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode(-1)
        pre = dummyHead

        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        if l1 is None:
            pre.next = l2
        else:
            pre.next = l1
        return dummyHead.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(5)
node8 = ListNode(6)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

s = Solution2()
head = s.mergeTwoLists(node1, node4)
while head:
    print(head.val)
    head = head.next
