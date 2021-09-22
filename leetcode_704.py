class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j = 0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] > target:
                j = mid-1
            elif nums[mid] < target:
                i = mid+1
            else:
                return mid
        return -1

s = Solution()
a = s.search([-1,0,3,5,9,12], 9)
print(a)
