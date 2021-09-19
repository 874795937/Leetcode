class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre1 = 1
        pre2 = 0
        result = 0
        for i in range(2, n+1):
            if i-2:
                pre2 = pre1
                pre1 = result
            result = pre1+pre2
            print(result, pre1, pre2)
        return result%(10**9+7)

s = Solution()
print(s.fib(5))
