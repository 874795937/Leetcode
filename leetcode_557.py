class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = []
        result = s.split(" ")
        for item in result:
            final.append("".join(list(reversed(item))))

        finalStr = " ".join(final)
        return finalStr
s = Solution()
a = s.reverseWords("Let's take LeetCode contest")
print(a)
