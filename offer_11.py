# j = j-1缩小范围
# i, j
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        i,j = 0, len(numbers)-1
        while i < j:
            mid = (i+j)//2
            if numbers[mid] > numbers[j]:
                i = mid+1
            elif numbers[mid] < numbers[j]:
                j = mid-1
            else:
                j = j-1
        return numbers[i]


s = Solution()
a = s.minArray([3,4,5,1,2])
print(a)
