class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if mat is None:
            return []
        rowNum = len(mat)
        columnNum =len(mat[0])
        queue = []
        for i in range(rowNum):
            for j in range(columnNum):
                if mat[i][j] == 0:
                    queue.append([i,j])
                if mat[i][j] == 1:
                    mat[i][j] = "#"

        if not queue or len(queue) == rowNum*columnNum:
            return mat

        distance = 0
        while queue:
            distance += 1
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                r = node[0]
                c = node[1]
                if r-1 >=0 and r-1<= rowNum-1 and c>=0 and c<=columnNum-1:
                    if mat[r-1][c] == "#":
                        mat[r-1][c] = distance
                        queue.append([r-1,c])
                if r+1 >=0 and r+1<= rowNum-1 and c>=0 and c<=columnNum-1:
                    if mat[r+1][c] == "#":
                        mat[r+1][c] = distance
                        queue.append([r+1,c])
                if r >=0 and r<= rowNum-1 and c+1>=0 and c+1<=columnNum-1:
                    if mat[r][c+1] == "#":
                        mat[r][c+1] = distance
                        queue.append([r,c+1])
                if r >=0 and r<= rowNum-1 and c-1>=0 and c-1<=columnNum-1:
                    if mat[r][c-1] == "#":
                        mat[r][c-1] = distance
                        queue.append([r,c-1])
        return mat
s = Solution()
s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
