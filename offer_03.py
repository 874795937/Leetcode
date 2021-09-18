# 哈希表方法
# 知识点：
# （1）python有set
# （2）判断集合是否有元素，用In
# （3）set有add, remove,
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        library = set()
        for i,item in enumerate(nums):
            if item not in library:
                library.add(item)
            else:
                return item

# 原地交换方法
# 将索引和值相互对应
class Solution1(object):
    def findRepeatNumber(self, nums):
        for i,elm in enumerate(nums):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    temp1 = nums[nums[i]]
                    temp2 = nums[i]
                    nums[i] = nums[temp]
                    nums[temp] = temp2

S = Solution1()
print(S.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
