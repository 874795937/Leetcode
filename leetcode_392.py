class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        if s == "":
            return True
        if t == "":
            return False

        for n in range(len(s)+len(t)):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i == len(s):
                    return True
                if j == len(t):
                    return False
            else:
                j += 1
                if j == len(t):
                    return False
        return False

class Solution1(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            print(i , j)
        # print(i)
        return i == len(s)

s = Solution1()
print(s.isSubsequence("abc","ahbgdc"))
