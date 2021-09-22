class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        i = 0
        j = 0
        while i <len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
        return result

class Solution1(object):
    def intersect(self, nums1, nums2):
        dic = {}
        result = []
        for item in nums1:
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1
        for item in nums2:
            if dic.get(item):
                if dic[item] > 0:
                    result.append(item)
                    dic[item] -= 1
        return result
        
s = Solution1()
a = s.intersect([4,9,5], [9,4,9,8,4])
print(a)
