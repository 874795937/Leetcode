# item.isalnum()--->判断是否是数字或字母
# item.lower()--->转化成小写

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        goodStr = ""
        for item in s:
            if item.isalnum():
                goodStr += item.lower()
        # print(goodStr)
        i = 0
        j = len(goodStr)-1
        while i != j and i < j:
            if goodStr[i] != goodStr[j]:
                return False
            j -= 1
            i += 1
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: aPanama"))
