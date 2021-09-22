class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i <= j:
            m = (i+j)//2
            # print(m)
            if nums[m] > target:
                j = m-1
            elif nums[m] < target:
                i = m+1
            else:
                return m
        return i
        
s = Solution()
a = s.searchInsert([1,3,5,6,7],2)
print(a)
    # i = 1, mid = 3, j = 6, target = 2
    # i = 1, mid = 1, j = 3, target = 2
    #
    # 1,2,3,4,5
