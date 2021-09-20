# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        dic = {}
        dummyHead = ListNode(-1)

        while head:
            value = head.val
            if value in seen:
                head = head.next
                continue
            else:
                dic[value] = head
                seen.add(value)
            head = head.next
        for i,item in enumerate(sorted(seen)):
            dic[item].next = None
            if i == 0:
                dummyHead.next = dic[item]
                pre = dic[item]
            else:
                pre.next = dic[item]
                pre = dic[item]
        return dummyHead.next

class Solution1():
    def deleteDuplicates(self, head):
        preValue = 0

node1 = ListNode(-1)
node2 = ListNode(0)
node3 = ListNode(0)
node4 = ListNode(0)
node5 = ListNode(3)
node6 = ListNode(3)
node7 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
head = s.deleteDuplicates(node1)
while head:
    print(head.val)
    head = head.next
