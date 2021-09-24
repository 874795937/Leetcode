class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix[0])
        if n == 0:
            return matrix[0][0]
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return min(matrix[0][0], matrix[0][1])+min(matrix[1][0], matrix[1][1])

        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])+matrix[i][j]

        result = dp[n-1][0]
        for i in range(n):
            result = min(result, dp[n-1][i])
        return result
s = Solution()
a = s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(a)
