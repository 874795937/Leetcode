# brute force method
#犯错的地方：j从i+1开始计算
class Solution:
    def twoSum(self, nums, target):
        result = [];
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sumNum = nums[i]+nums[j];
                if sumNum == target:
                    result.append(i);
                    result.append(j);
                    return result;

# hashmap method: dic in python
#易错的地方：
#  (1)for i,elm in enumerate();i是index, elm是value;
#  (2)此方法需要查找在除去这个数剩余的数中是否存在与差值相等的。
#  (3)dic就是hashmap
class Solution1:
    def twoSum(self, nums, target):
        hashmap = {}
        result = []
        for i,elm in enumerate(nums):
            hashmap[elm] = i;
        for j,item in enumerate(nums):
            temp = target - item
            index = hashmap.get(temp)
            if index is not None and j != index:
                result.append(j)
                result.append(index)
                return result

S = Solution1();
print(S.twoSum([3,3], 6));
