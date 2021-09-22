class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        for item in nums:
            if item == target:
                result += 1
        return result
#
class Solution1(object):
    def search(self, nums, target):
        i,j = 0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid+1
            elif nums[mid] > target:
                j = mid -1
            else:
                j = mid-1
        left = j
        print(left)

        i = 0
        j = len(nums)-1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        print(left)
        print(right)
        return right - left - 1

        # print(left)
        # result = right - left
        # return result


class Solution3:
    def search(self, nums: [int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        j = len(nums)-1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        print(left)
        print(right)
        return right - left - 1

s = Solution3()
a = s.search([5,7,3,8,8,10], 8)
print(a)
