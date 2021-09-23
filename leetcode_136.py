class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        repeated = []
        for item in nums:
            if item not in seen:
                seen.add(item)
            else:
                repeated.append(item)
        # print(repeated)
        for item in nums:
            if item not in repeated:
                return item
# 把if else写全避免出问题
class Solution1(object):
    def singleNumber(self, nums):
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if i == 0:
                pre = nums[i]
                # print("2333",i, pre)
            else:
                if nums[i] == pre:
                    pre = -1
                    # print(pre)
                elif nums[i] != pre and pre == -1:
                    print(pre, nums[i])
                    pre = nums[i]
                    # print(pre, nums[i])
        return pre


class Solution2(object):
    def singleNumber(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result
s = Solution2()
a = s.singleNumber([2,1,2])
print(a)
