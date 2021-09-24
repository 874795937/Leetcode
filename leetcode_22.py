class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.length = n
        result = []
        def dfs(path, left, right):
            if right > left or left > self.length or right > self.length:
                return
            if len(path) == 2*self.length:
                result.append(path)
                return
            else:
                dfs(path+"(", left+1, right)
                dfs(path+")", left, right+1)
        dfs("", 0, 0)
        return result

s = Solution()
a = s.generateParenthesis(3)
print(a)
