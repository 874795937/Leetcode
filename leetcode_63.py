class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    if i == 0 and j > 0:
                        dp[i][j] = dp[i][j-1]
                    if i > 0 and j == 0:
                        dp[i][j] = dp[i-1][j]
        return dp[m-1][n-1]


s = Solution()
a = s.uniquePathsWithObstacles([[0,0]])
print(a)
