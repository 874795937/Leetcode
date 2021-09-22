# 重复元素不适合set()
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        seen = set()
        result = ""
        num = 0
        for i in range(len(S)):
            if S[i] in seen:
                num += 1
            else:
                if num != 0:
                    result += str(num)
                seen.add(S[i])
                result += S[i]
                num = 1
        print(result)

class Solution(object):
    def compressString(self, S):
        result = ""
        num = 0
        for i in range(len(S)):
            if i == 0:
                result += S[i]
                pre = S[i]
                num = 1
            else:
                if pre != S[i]:
                    result += str(num)
                    result += S[i]
                    num = 1
                    pre = S[i]
                else:
                    num += 1
                    pre = S[i]
        result += str(num)
        print(result)
        if len(result) < len(S):
            return result
        else:
            return S

s = Solution()
s.compressString("aabcccccaaa")
