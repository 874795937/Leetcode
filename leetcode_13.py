# 哈希表方法
# 知识点：
# (1)python string可以被认作为list
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                   'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        result = 0
        check = 0
        for i in range(len(s)):
            if check == 0:
                temp = hashmap.get(s[i])
                if i+1 != len(s):
                    temp2 = hashmap.get(s[i+1])
                    if temp < temp2:
                        tempString = s[i]+s[i+1]
                        result += hashmap.get(tempString)
                        check = 1
                    else:
                        result += temp
                else:
                    result += temp
            else:
                check = 0
                continue
        return result

# 哈希表方法
# 知识点：
# （1）for i in range(len(s)-1)可以解决index outof bound 问题
class Solution1(object):
    def romanToInt(self, s):
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)-1):
            temp1 = hashmap.get(s[i])
            temp2 = hashmap.get(s[i+1])
            if temp1 < temp2:
                result -= temp1
            else:
                result += temp1
        result += hashmap.get(s[-1])
        return result
S = Solution1()
print(S.romanToInt("MCMXCIV"))
