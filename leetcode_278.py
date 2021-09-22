# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(version):
            if version == 1:
                return True
            else:
                return False
        i,j = 0, n-1
        answer = 0
        while i <= j:
            m =(i+j)//2
            if isBadVersion(m):
                j = m-1
            else:
                i = m+1
        return i

s = Solution()
a = s.firstBadVersion(1)
print(a)
# 1 2 3 4 5 6 7
