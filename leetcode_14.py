# 横向扫描
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = strs[0]

        def commonPart(str1, str2):
            result = ""
            length = min(len(str1), len(str2))
            for i in range(length):
                if str1[i] == str2[i]:
                    result += str1[i]
                else:
                    break
            return result

        for item in strs:
            result = commonPart(result, item)
        return result

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        result = strs[0]
        # print(result[0:3])
        minLength = len(strs[0])
        for value in strs:
            minLength = min(minLength, len(value))
        for i in range(minLength):
            for item in strs:
                if result[i] != item[i]:
                    return result[0:i]
        return result[0:minLength]



s = Solution()
print(s.longestCommonPrefix(["ab","a"]))
