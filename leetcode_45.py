class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        length = 0
        jump = 0
        while start < len(nums)-1:
            maxLength = 0
            temp = 0
            temp = nums[start]
            if start+nums[start] < len(nums)-1:
                for i in range(temp):
                    maxLength = max(maxLength, 1+i+nums[start+i+1])
                    if 1+i+nums[start+1+i] == maxLength:
                        temp = start+1+i
                start = temp

            else:
                start += nums[start]
            jump += 1
        return jump

class Solution(object):
    def jump(self, nums):
        j = 0
        dp = [0]*len(nums)
        for i in range(1, len(nums)):
            while nums[j]+j < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[len(nums)-1]

s = Solution()
a = s.jump([2,3,1])
print(a,"ans")
