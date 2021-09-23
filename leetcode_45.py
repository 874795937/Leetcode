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
            for i in range(nums[start]):
                maxLength = max(maxLength, i+nums[start+1+i])
                if i+nums[start+1+i] == maxLength:
                    start += 1+i
                if maxLength+start >= len(nums)-1:
                    start += 1+i
                    break
            jump += 1
        return jump

s = Solution()
a = s.jump([2,3,1,1,3,5,3])
print(a)
