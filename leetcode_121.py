class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0]*len(prices)
        minPrice = prices[0]
        for i in range(1,len(prices)):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i-1],prices[i]-minPrice)
        return dp[len(prices)-1]

class Solution1(object):
    def maxProfit(self, prices):
        maxNum = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxNum = max(maxNum, prices[i]-minPrice)
        return maxNum

S = Solution1()
print(S.maxProfit([7,1,5,3,6,4]))
