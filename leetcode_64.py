class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        dp = [[0 for i in range(m)] for j in range(n)]
        # road = []
        dp[0][0] = grid[0][0]
        # print(dp, m, n)
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                if i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                # road.append(grid[i][j])
        return dp[n-1][m-1]

s = Solution()
a = s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(a)
