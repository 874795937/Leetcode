class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None:
            return True
        x = str(x)
        i = 0
        j = len(x)-1
        while i < j and i != j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print(s.isPalindrome(1211))
