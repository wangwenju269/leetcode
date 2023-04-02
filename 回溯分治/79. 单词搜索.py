'''
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
'''
class solution:
      def process(self,board,word):
          m,n = len(board),len(board[0])
          for i in range(m):
              for j in range(n):
                  if board[i][j] == word[0]:
                     if  self.dfs(board,word[1:],i,j):
                         return True
          return False

      def dfs(self,board,word,i,j):
          if not word:
             return True
          m, n = len(board), len(board[0])
          c = board[i][j]
          board[i][j] = '#'
          for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
              if 0 <= x <m and 0 <= y < n and board[x][y] == word[0] \
                 and self.dfs(board,word[1:],x,y) :
                 return  True
          board[i][j] = c
          return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(solution().process(board,word))

