class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point = nums[0]
        i = 1
        length = len(nums)
        while i < len(nums):
            # print(nums[i])
            # print(nums[i], point,"2333")
            if nums[i] == point:
                # print(nums[i],"2444")
                # remove element
                for j in range(i, len(nums)):
                    if j == len(nums)-1:
                        nums.remove(nums[j])
                    else:
                        nums[j] = nums[j+1]
            else:
                point = nums[i]
                i += 1
        return nums

class Solution1(object):
    def removeDuplicates(self, nums):
        point = nums[0]
        check = 0
        for i in range(1,len(nums)):
            if point == nums[i]:
                nums[i] ="ii"
                check += 1
            else:
                point = nums[i]
        for j in range(check):
            nums.remove("ii")
        print(nums)
        return len(nums)

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        slowPoint = 1
        fastPoint = 1
        while fastPoint < len(nums):
            if nums[fastPoint] != nums[fastPoint-1]:
                nums[slowPoint] = nums[fastPoint]
                slowPoint += 1
            fastPoint += 1
        return slowPoint

s = Solution2()
nums = s.removeDuplicates([1,2,3,4,5,6])
print(nums)
