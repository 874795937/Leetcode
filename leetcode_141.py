# Definition for singly-linked list.
# (1) seen = set()
# (2) head.next = node1
# (3) 要判断是否有next
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 哈希表
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
                if not head.next:
                    return False
                else:
                    head = head.next
        return False

#快慢指针方法（龟兔赛跑）
# 如果兔子跑到底，则没有环
# 如果兔子在乌龟的后面，则有环
class Solution1(object):
    def hasCycle(self, head):
        slowPoint = head
        fastPoint = head.next
        while fastPoint:
            if slowPoint == fastPoint or fastPoint.next == slowPoint:
                return True
            else:
                slowPoint = slowPoint.next
                if not fastPoint.next:
                    return False
                else:
                    fastPoint = fastPoint.next.next
        return False

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
head.next = node1
node1.next = node2
node2.next = node3
# node3.next = node1
S = Solution1()
print(S.hasCycle(head))
