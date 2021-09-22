class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        dic = {}
        for i,item in enumerate(nums1):
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1
        # print(dic)
        for item in nums2:
            if dic.get(item):
                if dic[item] > 0:
                    dic[item] -= 1
                    result.append(item)
        # print(result)
        seen = set()
        result1 = []
        for item in result:
            if item not in seen:
                seen.add(item)
                result1.append(item)
        return result1
s = Solution()
a = s.intersection([1,2,2,1,3], [3,4,2,2])
print(a)
