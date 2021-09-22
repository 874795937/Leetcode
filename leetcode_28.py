class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "" and needle == "":
            return 0
        if needle == "":
            return 0
        needlePoint = 0
        haystackPoint = 0
        initial = 0
        while haystackPoint < len(haystack):
            if haystackPoint == len(haystack)-2:
                print(haystack[haystackPoint], needle[needlePoint])
            if haystack[haystackPoint] == needle[needlePoint]:
                if needlePoint == 0:
                    initial = haystackPoint
                needlePoint += 1
                # print("23333333333")
            else:
                if needlePoint != 0:
                    needlePoint = 0
                    haystackPoint = initial
            if needlePoint == len(needle):
                # print("244444")
                return haystackPoint-(len(needle)-1)
            haystackPoint += 1
        return -1

class Solution1(object):
    def strStr(self, haystack, needle):
        def getnext(a,needle):
            next=['' for i in range(a)]
            j,k=0,-1
            next[0]=k
            while(j<a-1):
                if k==-1 or needle[k]==needle[j]:
                    k+=1
                    j+=1
                    next[j]=k
                else:
                    k=next[k]
            return next
        next = getnext(len(needle), needle)
        if len(needle) == 0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if needle[j] == haystack[j] or j == -1:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == a:
            return i-j
        else:
            return -1

class Solution2(object):
    def strStr(self, haystack, needle):
        def next(length, needle):
            next = [0]*length
            j = 0
            next[0] = j
            for i in range(1, length):
                while j > 0 and needle[i] != needle[j]:
                    j = next[j-1]
                if needle[j] == needle[i]:
                    j += 1
                next[i] = j
            return next
        if needle == "":
            return 0
        next = next(len(needle), needle)


        j = 0
        for i in range(0, len(haystack)):
            while j > 0 and needle[j] != haystack[i]:
                j = next[j-1]
            if needle[j] == haystack[i]:
                j += 1
            if j == len(needle):
                return i-len(needle)+1
        return -1



s = Solution2()
num = s.strStr("","")
print(num)
