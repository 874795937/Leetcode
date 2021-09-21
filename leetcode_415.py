class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) < len(num1):
            temp = num1
            num1 = num2
            num2 = temp
        num1Length = len(num1)
        num2Length = len(num2)
        length = max(num1Length, num2Length)
        check = -1
        result = []
        add = 0
        for i in range(length):
            if i < len(num1):
                temp = int(num1[check])+int(num2[check])+add
            else:
                temp = int(num2[check])+add
            add = temp//10
            result.append(temp%10)
            check -= 1

        result = list(reversed(result))
        result = [str(integer) for integer in result]
        result = "".join(result)
        return result
s = Solution()
print(s.addStrings("0","9133"))
