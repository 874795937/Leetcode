class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        def maxMoney(nums):
            dp = [0]*length
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i],  dp[i-1])
            return dp[len(nums)-1]

        max1 = maxMoney(nums[1:length])
        max2 = maxMoney(nums[0:length-1])
        return max(max1, max2)

s = Solution()
a = s.rob([1,2,3,1])
print(a)
