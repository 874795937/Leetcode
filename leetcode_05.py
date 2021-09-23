class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        maxLength = 1
        begin = 0

        for j in range(1, len(s)):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    if j-1-(i+1)+1 < 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 >maxLength:
                    maxLength = j-i+1
                    begin = i
        # print()
        return s[begin:begin+maxLength]
s = Solution()
a = s.longestPalindrome("babad")
print(a)
