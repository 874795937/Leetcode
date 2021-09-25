
# 边界条件和不能是海里和不能是2
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowNum = len(grid)
        columnNum = len(grid[0])
        final = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r > rowNum-1 or c > columnNum-1:
                return 0

            if grid[r][c] != 1:
                return 0

            grid[r][c] = 2
            return 1+dfs(r-1, c)+dfs(r+1, c)+dfs(r, c+1)+dfs(r, c-1)

        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 1:
                    a = dfs(i, j)
                    final = max(a, final)
        return final

s = Solution()
a = s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(a)
