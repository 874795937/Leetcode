class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        num = len(nums)//2
        for i,item in enumerate(nums):
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1
        for item in dic:
            if dic[item] > num:
                return item
s = Solution()
a = s.majorityElement([2,2,1,1,1,2,2])
print(a)
