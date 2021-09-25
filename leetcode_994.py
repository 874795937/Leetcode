class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0

        queue = []
        rowNum = len(grid)
        columnNum = len(grid[0])
        check = 0
        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 2:
                    queue.append([i,j])
                if grid[i][j] == 1:
                    check =1
        # if not queue and grid[i][j] == 1:
        #     return -1
        # if not queue and grid[i][j] == 0:
        #     return 0
        if not queue:
            if check == 1:
                return -1
            else:
                return 0

        distance = 0
        while queue:
            distance += 1
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                r = node[0]
                c = node[1]
                if r-1>=0 and r-1<=rowNum-1 and c>=0 and c<=columnNum-1:
                    if grid[r-1][c] == 1:
                        grid[r-1][c] =2
                        queue.append([r-1,c])
                if r+1>=0 and r+1<=rowNum-1 and c>=0 and c<=columnNum-1:
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        queue.append([r+1,c])
                if r>=0 and r<=rowNum-1 and c-1>=0 and c-1<=columnNum-1:
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        queue.append([r,c-1])
                if r>=0 and r<=rowNum-1 and c+1>=0 and c+1<=columnNum-1:
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        queue.append([r,c+1])

        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 1:
                    return -1

        return distance-1
s = Solution()
a = s.orangesRotting([[1],[0]])
print(a)
