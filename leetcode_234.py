# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head:
            list.append(head.val)
            head = head.next
        print(list)
        if len(list)%2 == 1:
            temp = len(list)//2+1
        else:
            temp = len(list)//2
        i = 0
        j = -1
        while i < temp:
            if list[i] != list[j]:
                return False
            i += 1
            j -= 1
        return True

# 快慢指针可以帮助找到链表的中间值
# 快指针先走，慢指针后走
# 递归要设置全局变量
class Solution(object):
    def isPalindrome(self, head):
        self.result = None
        if head is None:
            return True
        point1 = head
        point2 = head

        while point2:
            # print(point1.val)
            point2 = point2.next
            if not point2:
                break
            point2 = point2.next
            point1 = point1.next

        # print(point1.val)
        def reverse(node, pre):
            # print(node.val)
            if node is None:
                self.result = pre
                # print(pre.val)
                return 0
            # print(node.val)
            nextNode = node.next
            node.next = pre
            pre = node
            reverse(nextNode, pre)
        # print(head.val)
        reverse(point1, None)
        # print(self.result.val)
        while self.result and head:
            if self.result.val != head.val:
                return False
            self.result = self.result.next
            head = head.next
        return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(3)
node6 = ListNode(2)
node7 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.isPalindrome(node1))
