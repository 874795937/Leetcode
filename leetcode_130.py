class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rowNum = len(board)
        columnNum = len(board[0])
        def dfs(board, r, c, index, check):
            if r < 0 or c < 0 or r > rowNum-1 or c > columnNum-1:
                return
            if board[r][c] != check:
                return
            board[r][c] = index
            dfs(board, r-1, c, index, check)
            dfs(board, r+1, c, index, check)
            dfs(board, r, c-1, index, check)
            dfs(board, r, c+1, index, check)

        for i in range(columnNum):
            dfs(board, 0, i, "#", "O")
        for i in range(columnNum):
            dfs(board, rowNum-1, i, "#", "O")
        for i in range(rowNum):
            dfs(board, i, 0, "#","O")
        for i in range(rowNum):
            dfs(board, i, columnNum-1, "#","O")

        for i in range(rowNum):
            for j in range(columnNum):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
                    
        for i in range(rowNum):
            print(board[i])
        return board

s = Solution()
s.solve([["O","O"],["O","O"]])
