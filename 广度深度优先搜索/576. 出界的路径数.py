'''
m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
'''
class solution:
      def process(self,m,n,maxMove,startRow,startColumn):
          pre_dp = [[0] * n for _ in range(m)]
          while maxMove:
               cur_dp = [[0] * n for _ in range(m)]
               for i in range(m):
                   for j in range(n):
                       for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                           x, y = i + dx, j + dy
                           if x < 0 or x >= m or y < 0 or y >= n:
                              cur_dp[i][j] += 1
                           else:
                              cur_dp[i][j] += pre_dp[x][y]
               pre_dp = cur_dp
               maxMove -= 1
          return pre_dp[startRow][startColumn] % 1000000007