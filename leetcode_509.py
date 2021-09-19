class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

class Solution(object):
    def fib(self, n):
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
            # print(result)
        return result

s = Solution()
print(s.fib(4))
