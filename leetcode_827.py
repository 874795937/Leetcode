import copy
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowNum = len(grid)
        columnNum = len(grid[0])
        final = 0
        def dfs(mygrid, r, c):
            if r < 0 or c < 0 or r > rowNum-1 or c > columnNum-1:
                return 0
            if mygrid[r][c] != 1:
                return 0
            mygrid[r][c] = 2
            return 1+dfs(mygrid,r-1,c)+dfs(mygrid,r+1,c)+dfs(mygrid,r,c+1)+dfs(mygrid,r,c-1)

        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 1:
                    tempGrid = copy.deepcopy(grid)
                    temp = dfs(tempGrid, i, j)
                    final = max(temp, final)
                elif grid[i][j] == 0:
                    mygrid = copy.deepcopy(grid)
                    mygrid[i][j] = 1
                    temp = dfs(mygrid, i, j)
                    final = max(temp, final)
        return final

class Solution(object):
    def largestIsland(self, grid):
        rowNum = len(grid)
        columnNum = len(grid[0])
        islandNum = 1
        numToArea = []
        final = 0
        check = 0

        def dfs(mygrid, r, c, islandNum):
            if r < 0 or c < 0 or r > rowNum-1 or c > columnNum-1:
                return 0
            if mygrid[r][c] != 1:
                return 0
            mygrid[r][c] = islandNum
            return 1+dfs(mygrid,r-1,c, islandNum)+dfs(mygrid,r+1,c,islandNum)+dfs(mygrid,r,c+1,islandNum)+dfs(mygrid,r,c-1,islandNum)

        def putArea(islandNum):
            for n in range(rowNum):
                for m in range(columnNum):
                    if grid[n][m] == "check":
                        grid[n][m] = islandNum

        def checkNegibour(i, j):
            seen = set()
            val = []
            area = 0
            if i-1 >= 0 and j >= 0 and i-1 <= rowNum-1 and j <= columnNum-1:
                val.append(grid[i-1][j])
            if i+1 >= 0 and j >= 0 and i+1 <= rowNum-1 and j <= columnNum-1:
                val.append(grid[i+1][j])
            if i >= 0 and j+1 >= 0 and i <= rowNum-1 and j+1 <= columnNum-1:
                val.append(grid[i][j+1])
            if i >= 0 and j-1 >= 0 and i <= rowNum-1 and j-1 <= columnNum-1:
                val.append(grid[i][j-1])
            for item in val:
                if item > 0:
                    if item not in seen:
                        seen.add(item)
            for item in seen:
                area += numToArea[item-2]
            return area+1

        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 1:
                    islandNum += 1
                    area = dfs(grid, i, j, islandNum)
                    numToArea.append(area)

        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 0:
                    tempArea = checkNegibour(i,j)
                    final = max(tempArea, final)
                    check +=1
        if check > 0:
            return final
        else:
            return rowNum*columnNum
s = Solution()
a = s.largestIsland([[1,0],[1,0]])
print(a)
