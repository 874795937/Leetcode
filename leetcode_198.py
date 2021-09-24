class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if length == 1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[length-1]

s = Solution()
a = s.rob([0])
print(a)
