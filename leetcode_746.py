class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        dp = [0]*len(cost)
        # print(dp)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
        return min(dp[length-1], dp[length-2])

s = Solution()
a = s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(a)
