class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        self.result = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r > row-1 or c > column-1:
                self.result += 1
                return 1

            if grid[r][c] == 0:
                self.result += 1
                return 1

            if grid[r][c] != 1:
                return 0

            grid[r][c] = 2
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return self.result


s = Solution()
a = s.islandPerimeter(grid = [[1,0]])
print(a)
