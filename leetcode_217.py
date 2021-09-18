class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for elm in nums:
            if elm in seen:
                return True
            else:
                seen.add(elm)
        return False


S = Solution()
print(S.containsDuplicate([1,2,3]))
