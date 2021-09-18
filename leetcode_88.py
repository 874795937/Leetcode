class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        list = []
        i = 0
        j = 0
        for b in range(m+n):
            if i == m:
                list.append(nums2[j])
                j += 1
            elif j == n:
                list.append(nums1[i])
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    list.append(nums1[i])
                    i += 1
                else:
                    list.append(nums2[j])
                    j += 1
        for a in range(m+n):
            nums1[a] = list[a]
        return nums1

class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        num = m+n-1
        for b in range(m+n):
            if j == -1:
                break
            elif i == -1:
                nums1[num] = nums2[j]
                j -= 1
                num -= 1
            else:
                if nums1[i] > nums2[j]:
                    nums1[num] = nums1[i]
                    i -= 1
                    num -= 1
                else:
                    nums1[num] = nums2[j]
                    j -= 1
                    num -= 1
        return nums1

S = Solution1()
print(S.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
