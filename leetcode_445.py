# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverse(pre, cur):
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        head1 = reverse(None, l1)
        head2 = reverse(None, l2)

        add = 0
        pre = None
        while head1 or head2 or add:
            if head1:
                head1val = head1.val
            else:
                head1val = 0
            if head2:
                head2val = head2.val
            else:
                head2val = 0
            head1Next = head1.next
            head2Next = head2.next
            node =ListNode(0)
            node.next = pre
            total = add+head1val+head2val
            if total >= 10:
                node.val = total%10
                add = 1
            else:
                node.val = total
                add = 0
            pre = node
            head1 = head1Next
            head2 = head2Next
        return pre

# node1 = ListNode(7)
node2 = ListNode(2)
# node3 = ListNode(4)
# node4 = ListNode(3)

node5 = ListNode(5)
# node6 = ListNode(6)
# node7 = ListNode(4)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# node5.next = node6
# node6.next = node7

s = Solution()
head = s.addTwoNumbers(node2, node5)

while head:
    print(head.val)
    head = head.next
