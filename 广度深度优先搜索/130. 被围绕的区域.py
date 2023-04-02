class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in [0,col-1]:
                if board[i][j] == 'O':
                   self.dfs(i,j,board)
        for i in [0,row-1]:
            for j in range(1,col-1):
                if board[i][j] == 'O':
                    self.dfs(i,j,board)
        for i in range(row):
            for j in range(col):
                    if board[i][j] == '*':
                       board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'
    def dfs(self,i,j,board):
        m = len(board)
        n = len(board[0])
        board[i][j] = '*'
        vec = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx, dy in vec:
            nx , ny = i+dx ,j + dy
            if  0  <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                self.dfs(nx, ny, board)
