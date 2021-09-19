class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            result = max(result, dp[i])
        return result

# 滚筒数组
class Solution1(object):
    def maxSubArray(self, nums):
        currentMax = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            previousMax = currentMax
            currentMax = max(previousMax+nums[i], nums[i])
            result = max(result, currentMax)
        return result

s = Solution1()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
