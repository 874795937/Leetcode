class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0 for i in range(j+1)] for j in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            # print(dp)
        minResult = dp[n-1][0]
        for item in dp[n-1]:
            minResult = min(minResult, item)
        return minResult
s = Solution()
a = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(a)
