# dynamic programming
# (1) 二维数组：dp = [[0 for i in range(1)] for j in range(2)]
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp= [[0 for i in range(j+1)] for j in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = 1
                elif j == i:
                    dp[i][j] =1
                else:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp

S = Solution()
print(S.generate(5))
# output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
