class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i,j = 0,x
        while i <= j:
            mid = (i+j)//2
            if mid*mid < x:
                i = mid+1
                # print(i,"iiii")
            elif mid*mid > x:
                j = mid-1
                # print(j,"jjjj")
            else:
                return mid
        return i-1
s = Solution()
a = s.mySqrt(9)
print(a)
# 1,2,3,4,5,6
# 0,1,2,3,4,5
