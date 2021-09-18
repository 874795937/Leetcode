# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 哈希表方法
# (1) return None
#（2）print(“{}”.format)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        while headA:
            if headA in seen:
                print("Intersected at '{}'".format(headA.val))
                return
            else:
                seen.add(headA)
                headA = headA.next

        while headB:
            if headB in seen:
                print("Intersected at '{}'".format(headB.val))
                return
            else:
                seen.add(headB)
                headB = headB.next
        return None

# 双指针方法
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        point1 = headA
        point2 = headB

        while point1 != point2:
            if not point1.next and not point2.next:
                return None

            if point1.next:
                point1 = point1.next
            else:
                point1 = headB

            if point2.next:
                point2 = point2.next
            else:
                point2 = headA
        return point1

a1 = ListNode(1)
a2 = ListNode(2)
b1 = ListNode(3)
b2 = ListNode(4)
b3 = ListNode(8)
c1 = ListNode(5)
c2 = ListNode(6)
c3 = ListNode(7)
a1.next = a2
b1.next = b2
# a2.next = c1
b2.next = b3
# b3.next = c1
# c1.next = c2
# c2.next = c3
S = Solution1()
S.getIntersectionNode(a1, a2)
