# (1) bin()
# (2) string.count('a',0)
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            temp = str(bin(i))
            num = temp.count('1',0)
            result.append(num)
        return result

# dynamic programming
class Solution1(object):
    def countBits(self, n):
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        if n%2 == 0:
            size = n//2+1
        elif n%2 != 0:
            size = (n+1)//2

        for i in range(size):
            dp[2*i] = dp[i]
            if 2*i+1 <= n:
                dp[2*i+1] = dp[i]+1
        return dp

S = Solution1()
print(S.countBits(5))
