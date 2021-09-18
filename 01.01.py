# hashset 方法
class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        seen = set()
        for elm in astr:
            if elm in seen:
                return True
            else:
                seen.add(elm)
        return False

S = Solution()
print(S.isUnique("leetcode"))
