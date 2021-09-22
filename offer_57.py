# dic.get()
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        result = []
        for i,item in enumerate(nums):
            dic[item] = i
        # print(dic)
        for item in nums:
            num = target - item
            if dic.get(num):
                result.append(num)
                result.append(item)
                return result

class Solution1(object):
    def twoSum(self, nums, target):
        seen = set()
        result = []
        for item in nums:
            seen.add(item)
        # print(seen)
        for item in nums:
            num = target-item
            if num in seen:
                result.append(num)
                result.append(item)
                return result
s = Solution1()
result = s.twoSum([2,7,11,15,11], 9)
print(result)
