class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1")+bin(j).count("1") == turnedOn:
                    if j >= 10:
                        result.append(str(i)+":"+str(j))
                    else:
                        result.append(str(i)+":0"+str(j))
        return result
s = Solution()
s.readBinaryWatch(1)
