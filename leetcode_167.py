# return 在循环里
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        result = [0]*2
        for i,item in enumerate(numbers):
            dic[item] = i
        print(dic)
        for i,item in enumerate(numbers):
            num = target - item
            if dic.get(num):
                # print(i,"iii")
                result[0] = i+1
                result[1] = dic.get(num)+1
                return result

s = Solution()
a = s.twoSum([2,3,4], 6)
print(a)
