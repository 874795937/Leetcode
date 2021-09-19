class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        dp = [[0 for j in range(i+1)] for i in range(rowIndex)]
        for i in range(rowIndex):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = 1
                elif j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp[rowIndex-1]

S = Solution()
print(S.getRow(5))
