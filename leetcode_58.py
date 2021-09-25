class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result =s.split(" ")
        final = []
        for item in result:
            if item != "":
                final.append(item)
        return(len(final[-1]))
s = Solution()
a = s.lengthOfLastWord("   fly me   to   the moon  ")
print(a)
