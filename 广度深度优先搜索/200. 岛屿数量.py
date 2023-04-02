'''
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
'''
class solution:
      def process(self,grid):
          m , n = len(grid) ,len(grid[0])
          count = 0
          for i in range(m):
              for j in range(n):
                  if grid[i][j] == '1':
                     count += 1
                     self.dfs(grid,i,j)
          return count
      def dfs(self,grid,i,j):
          m, n = len(grid), len(grid[0])
          grid[i][j] = '0'
          for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
              if 0<= x<m and 0<= y < n and grid[x][y] == '1':
                 self.dfs(grid,x,y)
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution().process(grid))