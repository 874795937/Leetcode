# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# hashset
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        while headA:
            if headA in seen:
                # print(headA.val)
                return headA
            else:
                seen.add(headA)
                headA = headA.next

        while headB:
            if headB in seen:
                # print(headB.val)
                return headB
            else:
                seen.add(headB)
                headB = headB.next
        return None

# double points
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        point1 = headA
        point2 = headB
        while point1 != point2:
            if not point1.next and not point2.next:
                return None
            else:
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
a3 = ListNode(3)
b1 = ListNode(4)
b2 = ListNode(5)
c1 = ListNode(6)
c2 = ListNode(7)

a1.next = a2
a2.next = a3
a3.next = c1
b1.next = b2
b2.next = c1
c1.next = c2
S = Solution1()
print(S.getIntersectionNode(a1, b1))
