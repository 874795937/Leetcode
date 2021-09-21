class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums)
        for i in range(slow, len(nums)):
            nums[i] = 0
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])
