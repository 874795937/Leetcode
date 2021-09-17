# 知识点：数字翻转可以不用stack，取模就可以
# 判断是否越界，可以从倒数第二个开始比较。
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -1*x
            check = -1
        else:
            check = 1
        result = 0
        while x != 0:
            temp = x%10
            if (check == -1) and (result > 214748364 or (result == 214748364 and temp > 8)):
                return 0
            if (check == 1) and (result >214748364 or (result == 214748364 and temp > 7)):
                return 0
            result = result*10+temp
            x //= 10
        return result*check

S = Solution()
print(S.reverse(-123))
