# （1）边界条件
# （2）循环停止条件是：两个指针中有的小于零
# （3）如果A指针先到达了0，那么需要将B中剩余的拷贝到A中
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        if m == 0:
            for i in range(len(A)):
                A[i] = B[i]
        elif n == 0:
            print("")
        else:
            pointA = m-1
            pointB = n-1
            i = m+n-1
            while pointA >= 0 and pointB >= 0:
                if A[pointA] < B[pointB]:
                    A[i] = B[pointB]
                    pointB -= 1
                else:
                    A[i] = A[pointA]
                    pointA -= 1
                i -= 1
            # print(A)
            if pointA < pointB:
                while pointB >= 0:
                    A[pointB] = B[pointB]
                    pointB -= 1
        # print(A)

s = Solution()
s.merge( [1,2,3,0,0,0], 3, [4,5,6], 3)
