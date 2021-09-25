class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowNum = len(grid)
        columnNum = len(grid[0])

        def bfs(node):
            queue = []
            result = []
            queue.append(node)
            while queue:
                length = len(queue)
                temp = []
                for i in range(length):
                    node = queue.pop(0)
                    temp.append(node)
                    r = node[0]
                    c = node[1]
                    if r-1 >= 0 and r-1 <= rowNum-1 and c >= 0 and c <= columnNum-1:
                        if grid[r-1][c] == 0:
                            grid[r-1][c] = 2
                            queue.append([r-1, c])
                    if r+1 >= 0 and r+1 <= rowNum-1 and c >= 0 and c <= columnNum-1:
                        if grid[r+1][c] == 0:
                            grid[r+1][c] = 2
                            queue.append([r+1, c])
                    if r >= 0 and r <= rowNum-1 and c+1 >= 0 and c+1 <= columnNum-1:
                        if grid[r][c+1] == 0:
                            grid[r][c+1] = 2
                            queue.append([r, c+1])
                    if r >= 0 and r <= rowNum-1 and c-1 >= 0 and c-1 <= columnNum-1:
                        if grid[r][c-1] == 0:
                            grid[r][c-1] = 2
                            queue.append([r, c-1])
                result.append(temp)
            return result

        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    result = bfs([i,j])
                    print(result)
                    print(grid)
                    return result

class Solution1(object):
    def maxDistance(self, grid):
        rowNum = len(grid)
        columnNum = len(grid[0])
        queue = []
        for i in range(rowNum):
            for j in range(columnNum):
                if grid[i][j] == 1:
                    queue.append([i,j])

        if not queue or len(queue) == rowNum*columnNum:
            return -1

        distance = 0
        while queue:
            distance += 1
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                r = node[0]
                c = node[1]
                if r-1 >= 0 and r-1 <= rowNum-1 and c >= 0 and c <= columnNum-1:
                    if grid[r-1][c] == 0:
                        grid[r-1][c] = 2
                        queue.append([r-1, c])
                if r+1 >= 0 and r+1 <= rowNum-1 and c >= 0 and c <= columnNum-1:
                    if grid[r+1][c] == 0:
                        grid[r+1][c] = 2
                        queue.append([r+1, c])
                if r >= 0 and r <= rowNum-1 and c+1 >= 0 and c+1 <= columnNum-1:
                    if grid[r][c+1] == 0:
                        grid[r][c+1] = 2
                        queue.append([r, c+1])
                if r >= 0 and r <= rowNum-1 and c-1 >= 0 and c-1 <= columnNum-1:
                    if grid[r][c-1] == 0:
                        grid[r][c-1] = 2
                        queue.append([r, c-1])
        return distance-1

s = Solution1()
a = s.maxDistance([[1,0,0],[0,0,0],[0,0,0]])
print(a)
