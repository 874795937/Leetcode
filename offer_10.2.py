class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*n
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[n-1]%(10**9+7)

s = Solution()
print(s.numWays(7))
